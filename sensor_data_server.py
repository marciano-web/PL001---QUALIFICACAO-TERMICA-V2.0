#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor Flask para processamento de dados de sensores
Processa dados no backend para reduzir consumo de memória do navegador
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import re
from collections import defaultdict
import sys
import os

app = Flask(__name__)
CORS(app)  # Permitir requisições do frontend

def parse_custom_date(date_str, date_format='english'):
    """
    Converte string de data para timestamp
    """
    if not date_str or not isinstance(date_str, str):
        return None
    
    date_str = date_str.strip()
    
    try:
        if date_format == 'portuguese':
            # Formato: DD-MM-YY HH:MM:SS
            match = re.match(r'(\d{2})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})', date_str)
            if match:
                day, month, year, hours, minutes, seconds = match.groups()
                full_year = f"20{year}" if int(year) < 70 else f"19{year}"
                dt = datetime(int(full_year), int(month), int(day), 
                            int(hours), int(minutes), int(seconds))
                return int(dt.timestamp() * 1000)  # Retornar em milissegundos
        else:  # english
            # Formato: YYYY-MM-DD HH:MM:SS
            match = re.match(r'(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})', date_str)
            if match:
                year, month, day, hours, minutes, seconds = match.groups()
                dt = datetime(int(year), int(month), int(day), 
                            int(hours), int(minutes), int(seconds))
                return int(dt.timestamp() * 1000)  # Retornar em milissegundos
    except Exception as e:
        print(f"Erro ao parsear data '{date_str}': {e}", file=sys.stderr)
        return None
    
    return None

@app.route('/api/process-sensors', methods=['POST'])
def process_sensors():
    """
    Endpoint principal para processar dados de sensores
    
    Recebe:
    {
        "sensors": [
            {
                "id": "sensor1",
                "sensorId": "DLH-176",
                "data": "2024-01-01 10:00:00|25.5|60.2\n..."
            },
            ...
        ],
        "dataType": "temp" | "humid" | "both",
        "dateFormat": "english" | "portuguese",
        "startDate": timestamp (opcional),
        "endDate": timestamp (opcional),
        "allDates": true | false
    }
    
    Retorna:
    {
        "timestamps": [timestamp1, timestamp2, ...],
        "dataPoints": {
            "timestamp1": {
                "sensor1": value,
                "sensor2": value,
                ...
            },
            ...
        }
    }
    """
    try:
        data = request.json
        sensors = data.get('sensors', [])
        data_type = data.get('dataType', 'temp')
        date_format = data.get('dateFormat', 'english')
        start_date = data.get('startDate')
        end_date = data.get('endDate')
        all_dates = data.get('allDates', True)
        
        if not sensors:
            return jsonify({'error': 'Nenhum sensor fornecido'}), 400
        
        # Estruturas para armazenar dados processados
        all_timestamps = set()
        all_data_points = defaultdict(dict)
        
        # Processar cada sensor
        for sensor in sensors:
            sensor_key = sensor.get('id')
            sensor_data = sensor.get('data', '')
            
            if not sensor_key or not sensor_data:
                continue
            
            # Processar linhas de dados
            lines = sensor_data.strip().split('\n')
            for line in lines:
                if not line.strip():
                    continue
                
                parts = line.split('|')
                if len(parts) < 2:
                    continue
                
                # Parsear data
                timestamp = parse_custom_date(parts[0], date_format)
                if not timestamp:
                    continue
                
                all_timestamps.add(timestamp)
                
                # Processar valores baseado no tipo de dados
                try:
                    if data_type == 'temp':
                        value = float(parts[1]) if len(parts) > 1 else None
                        if value is not None:
                            all_data_points[timestamp][sensor_key] = value
                    
                    elif data_type == 'humid':
                        value = float(parts[1]) if len(parts) > 1 else None
                        if value is not None:
                            all_data_points[timestamp][sensor_key] = value
                    
                    elif data_type == 'both':
                        temp_value = float(parts[1]) if len(parts) > 1 and parts[1].strip() else None
                        humid_value = float(parts[2]) if len(parts) > 2 and parts[2].strip() else None
                        
                        if temp_value is not None:
                            all_data_points[timestamp][f"{sensor_key}_temp"] = temp_value
                        if humid_value is not None:
                            all_data_points[timestamp][f"{sensor_key}_humid"] = humid_value
                
                except (ValueError, IndexError) as e:
                    # Ignorar linhas com valores inválidos
                    continue
        
        if not all_timestamps:
            return jsonify({'error': 'Não foram encontrados dados válidos'}), 400
        
        # Ordenar timestamps
        sorted_timestamps = sorted(list(all_timestamps))
        
        # Aplicar filtro de data se necessário
        if not all_dates and start_date and end_date:
            sorted_timestamps = [
                ts for ts in sorted_timestamps 
                if start_date <= ts <= end_date
            ]
            
            if not sorted_timestamps:
                return jsonify({'error': 'Não há dados no intervalo de datas selecionado'}), 400
        
        # Converter para formato JSON-friendly
        result = {
            'timestamps': sorted_timestamps,
            'dataPoints': {
                str(ts): all_data_points[ts] 
                for ts in sorted_timestamps
            },
            'totalPoints': len(sorted_timestamps),
            'totalSensors': len(sensors)
        }
        
        return jsonify(result)
    
    except Exception as e:
        print(f"Erro no processamento: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Erro no servidor: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se o servidor está funcionando"""
    return jsonify({'status': 'ok', 'message': 'Servidor Flask funcionando!'})

if __name__ == '__main__':
    print("=" * 60)
    print("Servidor Flask para Processamento de Dados de Sensores")
    print("=" * 60)
    print("\nServidor iniciado em: http://localhost:5000")
    print("\nEndpoints disponíveis:")
    print("  - GET  /api/health          - Verificar status do servidor")
    print("  - POST /api/process-sensors - Processar dados de sensores")
    print("\nPressione Ctrl+C para parar o servidor")
    print("=" * 60)
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

