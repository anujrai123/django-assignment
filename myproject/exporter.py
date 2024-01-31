
import csv
from pilotlog.models import Aircraft, Pilot

def export_data_to_csv(file_path='export - logbook_template.csv'):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
          
            writer = csv.writer(csvfile)

          
            writer.writerow(['ForeFlight Logbook Import'])
            writer.writerow([])

           
            writer.writerow(['Aircraft Table'])
            writer.writerow(['Text', 'Text', 'Text', 'YYYY', 'Text', 'Text', 'Text', 'Text', 'Text', 'Text',
                             'Boolean', 'Boolean', 'Boolean', 'Boolean'])
            writer.writerow(['AircraftID', 'EquipmentType', 'TypeCode', 'Year', 'Make', 'Model', 'Category', 'Class',
                             'GearType', 'EngineType', 'Complex', 'HighPerformance', 'Pressurized', 'TAA'])
            
            for aircraft in Aircraft.objects.all():
                writer.writerow([aircraft.id, aircraft.field1, aircraft.field2, ...])  

          
            writer.writerow(['Flights Table'])
            writer.writerow(['Date', 'Text', 'Text', 'Text', 'Text', 'hhmm', 'hhmm', 'hhmm', 'hhmm', 'hhmm', 'hhmm',
                             'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Number',
                             'Decimal', 'Number', 'Number', 'Number', 'Number', 'Number', 'Decimal', 'Decimal', 'Decimal',
                             'Decimal', 'Decimal', 'Decimal', 'Number', 'Packed Detail', 'Packed Detail', 'Packed Detail',
                             'Packed Detail', 'Packed Detail', 'Packed Detail', 'Decimal', 'Decimal', 'Decimal', 'Decimal',
                             'Text', 'Text', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail',
                             'Packed Detail', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Text', 'Decimal',
                             'Decimal', 'Number', 'Date', 'DateTime', 'Boolean', 'Text'])
            
            for flight in Flight.objects.all():
                writer.writerow([flight.date, flight.field1, flight.field2, ...]) 

        print(f'Data exported to CSV: {file_path}')
    except Exception as e:
        print(f'Error exporting data to CSV: {e}')
