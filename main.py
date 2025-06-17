import pandas as pd
import os
from pathlib import Path
import numpy as np

class CSVNormalizer:
    def __init__(self, data_folder='data'):
        self.data_folder = Path(data_folder)
        self.output_columns = [
            'fullname', 'email', 'user', 'application', 
            'C_JURIS', 'XL_INSTITUCION', 'C_UNID_EJEC', 'XL_UNID_EJEC'
        ]
        
    def read_csv_safe(self, filepath, encoding='utf-8', delimiter=','):
        """Lee CSV con manejo de errores y diferentes encodings"""
        encodings_to_try = [encoding, 'utf-8', 'cp1252', 'latin1']
        
        for enc in encodings_to_try:
            try:
                return pd.read_csv(filepath, encoding=enc, delimiter=delimiter)
            except (UnicodeDecodeError, pd.errors.ParserError):
                continue
        
        raise Exception(f"No se pudo leer el archivo {filepath} con ningún encoding")
    
    def process_sigaf_internos(self, filepath):
        """Procesa SIGAF_CONSULTA_1202506121604.csv (SIGAF Internos)"""
        print(f"Procesando SIGAF Internos: {filepath}")
        
        # El archivo tiene comillas dobles anidadas, necesita procesamiento especial
        df = self.read_csv_safe(filepath, delimiter=',')
        
        # Limpiar nombres de columnas de comillas extra
        df.columns = [col.strip('"') for col in df.columns]
        
        normalized_data = []
        for _, row in df.iterrows():
            normalized_row = {
                'fullname': str(row.get('XC_USER', '')).strip('"'),
                'email': str(row.get('XL_EMAIL', '')).strip('"'),
                'user': str(row.get('C_USER', '')).strip('"'),
                'application': 'SIGAF Internos',
                'C_JURIS': str(row.get('C_JURIS', '')).strip('"'),
                'XL_INSTITUCION': str(row.get('XL_INSTITUCION', '')).strip('"'),
                'C_UNID_EJEC': str(row.get('C_UNID_EJEC', '')).strip('"'),
                'XL_UNID_EJEC': str(row.get('XL_UNID_EJEC', '')).strip('"')
            }
            normalized_data.append(normalized_row)
        
        return pd.DataFrame(normalized_data)
    
    def process_mia_consulta(self, filepath):
        """Procesa MIA_CONSULTA_1202506121540.csv"""
        print(f"Procesando MIA: {filepath}")
        
        df = self.read_csv_safe(filepath, delimiter=',')
        
        # Limpiar nombres de columnas de comillas extra
        df.columns = [col.strip('"') for col in df.columns]
        
        normalized_data = []
        for _, row in df.iterrows():
            # Combinar FirstName y LastName
            first_name = str(row.get('FirstName', '')).strip('"')
            last_name = str(row.get('LastName', '')).strip('"')
            full_name = f"{first_name} {last_name}".strip()
            
            normalized_row = {
                'fullname': full_name,
                'email': str(row.get('Email', '')).strip('"'),
                'user': str(row.get('UserName', '')).strip('"'),
                'application': 'MIA',
                'C_JURIS': None,
                'XL_INSTITUCION': None,
                'C_UNID_EJEC': None,
                'XL_UNID_EJEC': None
            }
            normalized_data.append(normalized_row)
        
        return pd.DataFrame(normalized_data)
    
    def process_sigaf_externos(self, filepath):
        """Procesa SIGAF_CONSULTA_2202506121605.csv (SIGAF Externos)"""
        print(f"Procesando SIGAF Externos: {filepath}")
        
        df = self.read_csv_safe(filepath, delimiter=',')
        
        # Limpiar nombres de columnas de comillas extra
        df.columns = [col.strip('"') for col in df.columns]
        
        normalized_data = []
        for _, row in df.iterrows():
            normalized_row = {
                'fullname': str(row.get('XL_ENTE', '')).strip('"'),
                'email': str(row.get('XL_MAIL', '')).strip('"'),
                'user': str(row.get('N_CUIT', '')).strip('"'),
                'application': 'SIGAF Externos',
                'C_JURIS': None,
                'XL_INSTITUCION': None,
                'C_UNID_EJEC': None,
                'XL_UNID_EJEC': None
            }
            normalized_data.append(normalized_row)
        
        return pd.DataFrame(normalized_data)
    
    def process_bac_externos(self, filepath):
        """Procesa bac mails2.csv (BAC Externos)"""
        print(f"Procesando BAC Externos: {filepath}")
        
        df = self.read_csv_safe(filepath, delimiter=';')
        
        normalized_data = []
        for _, row in df.iterrows():
            # Combinar Nombre y Apellido, o usar RazonSocial si está disponible
            if pd.notna(row.get('RazonSocial')) and row.get('RazonSocial') != 'NULL':
                fullname = str(row.get('RazonSocial', ''))
            else:
                nombre = str(row.get('Nombre', ''))
                apellido = str(row.get('Apellido', ''))
                fullname = f"{nombre} {apellido}".strip()
            
            normalized_row = {
                'fullname': fullname,
                'email': str(row.get('LoweredEmail', '')),
                'user': str(row.get('usuario', '')),
                'application': 'BAC Externos',
                'C_JURIS': None,
                'XL_INSTITUCION': None,
                'C_UNID_EJEC': None,
                'XL_UNID_EJEC': None
            }
            normalized_data.append(normalized_row)
        
        return pd.DataFrame(normalized_data)
    
    def process_bac_internos(self, filepath):
        """Procesa mails bac1.csv (BAC Internos)"""
        print(f"Procesando BAC Internos: {filepath}")
        
        df = self.read_csv_safe(filepath, delimiter=';')
        
        normalized_data = []
        for _, row in df.iterrows():
            # Combinar Nombre y Apellido
            nombre = str(row.get('Nombre', ''))
            apellido = str(row.get('Apellido', ''))
            fullname = f"{nombre} {apellido}".strip()
            
            normalized_row = {
                'fullname': fullname,
                'email': str(row.get('LoweredEmail', '')),
                'user': str(row.get('usuario', '')),
                'application': 'BAC Internos',
                'C_JURIS': None,
                'XL_INSTITUCION': None,
                'C_UNID_EJEC': None,
                'XL_UNID_EJEC': None
            }
            normalized_data.append(normalized_row)
        
        return pd.DataFrame(normalized_data)
    
    def process_all_files(self):
        """Procesa todos los archivos CSV y los consolida"""
        
        # Verificar que existe la carpeta data
        if not self.data_folder.exists():
            raise Exception(f"La carpeta {self.data_folder} no existe")
        
        consolidated_data = []
        
        # Mapeo de archivos a funciones de procesamiento
        file_processors = {
            'SIGAF_CONSULTA_1202506121604.csv': self.process_sigaf_internos,
            'MIA_CONSULTA_1202506121540.csv': self.process_mia_consulta,
            'SIGAF_CONSULTA_2202506121605.csv': self.process_sigaf_externos,
            'bac mails2.csv': self.process_bac_externos,
            'mails bac1.csv': self.process_bac_internos
        }
        
        # Procesar cada archivo
        for filename, processor in file_processors.items():
            filepath = self.data_folder / filename
            
            if filepath.exists():
                try:
                    df_processed = processor(filepath)
                    consolidated_data.append(df_processed)
                    print(f"✓ Procesado exitosamente: {filename} ({len(df_processed)} registros)")
                except Exception as e:
                    print(f"✗ Error procesando {filename}: {str(e)}")
            else:
                print(f"⚠ Archivo no encontrado: {filename}")
        
        # Consolidar todos los DataFrames
        if consolidated_data:
            final_df = pd.concat(consolidated_data, ignore_index=True)
            
            # Limpiar datos
            final_df = self.clean_data(final_df)
            
            return final_df
        else:
            raise Exception("No se pudieron procesar archivos")
    
    def clean_data(self, df):
        """Limpia y normaliza los datos consolidados"""
        print("Limpiando datos...")
        
        # Reemplazar valores vacíos, 'NULL', 'nan' con None
        df = df.replace(['NULL', 'nan', '', 'None', '.'], None)
        
        # Limpiar espacios en blanco extra
        string_columns = ['fullname', 'email', 'user', 'application', 
                         'XL_INSTITUCION', 'XL_UNID_EJEC']
        
        for col in string_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
                df[col] = df[col].replace('nan', None)
        
        # Convertir emails a minúsculas
        df['email'] = df['email'].str.lower()
        
        return df
    
    def save_to_excel(self, df, output_filename='normalized_data.xlsx'):
        """Guarda el DataFrame consolidado a Excel"""
        output_path = Path(output_filename)
        
        try:
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Consolidated_Data', index=False)
            
            print(f"✓ Archivo Excel guardado exitosamente: {output_path}")
            print(f"Total de registros: {len(df)}")
            
            # Mostrar resumen por aplicación
            print("\nResumen por aplicación:")
            summary = df.groupby('application').size().reset_index(name='count')
            for _, row in summary.iterrows():
                print(f"  - {row['application']}: {row['count']} registros")
                
        except Exception as e:
            print(f"✗ Error guardando archivo Excel: {str(e)}")
    
    def run(self, output_filename='normalized_data.xlsx'):
        """Ejecuta todo el proceso de normalización"""
        print("Iniciando proceso de normalización de CSV...")
        print("="*50)
        
        try:
            # Procesar todos los archivos
            consolidated_df = self.process_all_files()
            
            print("="*50)
            print("Datos consolidados exitosamente")
            
            # Guardar a Excel
            self.save_to_excel(consolidated_df, output_filename)
            
            print("="*50)
            print("Proceso completado exitosamente!")
            
            return consolidated_df
            
        except Exception as e:
            print(f"✗ Error en el proceso: {str(e)}")
            return None

def main():
    """Función principal"""
    # Crear instancia del normalizador
    normalizer = CSVNormalizer(data_folder='data')
    
    # Ejecutar el proceso
    result_df = normalizer.run('consolidated_data.xlsx')
    
    # Mostrar muestra de los datos si todo salió bien
    if result_df is not None:
        print("\nMuestra de los primeros 5 registros:")
        print(result_df.head().to_string())

if __name__ == "__main__":
    main()