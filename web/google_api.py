import io
import os
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
try:
    from google_service import Create_Service
except:
    pass

def service_google(Create_Service):
    CLIENT_SECRET_FILE = os.path.join(os.getcwd(),'web','client_secret.json')
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    return service

class Base():
    def __init__(self) :
        pass

    def crear_file(self,Create_Service):
        service = service_google(Create_Service)
        folder = '1u3N-ci47hXqwroe1EvtkOeTjKXwNUTcR'
        file_metadata = {
            'name': 'base.db',
            'parents': folder
        }
        path_base = os.path.join(os.getcwd(),'base','base.db')
        media_content = MediaFileUpload(path_base, mimetype='application/x-sqlite3')
        file = service.files().create(
            body=file_metadata,
            media_body=media_content
        ).execute()
        print(file)


    def update_file(self,Create_Service):
        service = service_google(Create_Service)
        file_id = "1lXrQwvWC2F0HxM7RZqo5RbxtGhbz8XBI"
        path_base = os.path.join(os.getcwd(),'base','base.db')
        media_content = MediaFileUpload(path_base, mimetype='application/x-sqlite3')
        service.files().update(
            fileId=file_id,
            media_body=media_content
        ).execute()

    def download_file(self,Create_Service):
        service = service_google(Create_Service)
        file_id = "1lXrQwvWC2F0HxM7RZqo5RbxtGhbz8XBI"
        file_name = 'base.db'
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh,request=request)
        done = False
        while not done:
            status,done = downloader.next_chunk()
            print('download progress {}'.format(status.progress()))
        fh.seek(0)
        path_base = os.path.join(os.getcwd(),'base')
        with open(os.path.join(path_base,file_name),'wb') as f:
            f.write(fh.read())
            f.close

    def download_file_compare(self,Create_Service):
        service = service_google(Create_Service)
        file_id = "1lXrQwvWC2F0HxM7RZqo5RbxtGhbz8XBI"
        file_name = 'base_compare.db'
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh,request=request)
        done = False
        while not done:
            status,done = downloader.next_chunk()
            print('download progress {}'.format(status.progress()))
        fh.seek(0)
        path_base = os.path.join(os.getcwd(),'base')
        with open(os.path.join(path_base,file_name),'wb') as f:
            f.write(fh.read())
            f.close
         

class Sheets():
    def __init__(self) :
        pass

    def crear_file(self,name,Create_Service):
        service = service_google(Create_Service)
        folder = '1u3N-ci47hXqwroe1EvtkOeTjKXwNUTcR'
        file_metadata = {
            'name': 'Inventario',
            'parents': folder
        }
        path_base = os.path.join(os.getcwd(),'exports',name)
        media_content = MediaFileUpload(path_base, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file = service.files().create(
            body=file_metadata,
            media_body=media_content
        ).execute()
        print(file)


    def update_file(self,name,Create_Service):
        service = service_google(Create_Service)
        file_id = "1z0J8mFXt45a50tuYaGhBY1IPSgczAQnx"
        path_base = os.path.join(name)
        media_content = MediaFileUpload(path_base, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        service.files().update(
            fileId=file_id,
            media_body=media_content
        ).execute()

class Fotos():

    def __init__(self):
        self.folder = '14o2GxGaJJ2souvG0caD68yKLzN9T8iw6'

    def create_file(self,codigo,Create_Service):
        service = self.service_google(Create_Service)
        codigo =  codigo + '.jpg'
        path_foto = os.path.join(os.getcwd(),'src','img-codigos',codigo)
        file_metadata = {
            'name': codigo,
            'parents': [self.folder]
        }
        media_content = MediaFileUpload(path_foto, mimetype='image/jpeg')
        file = service.files().create(
            body=file_metadata,
            media_body=media_content,
            fields='id'
        ).execute()
        id = file['id']
        return (codigo.replace('.jpg',''),id)



    def download_foto(self,codigo,id,Create_Service):
        service = self.service_google(Create_Service)
        file_id = id
        file_name = codigo + '.jpg'
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh,request=request)
        done = False
        while not done:
            status,done = downloader.next_chunk()
            print('download progress {}'.format(status.progress()))
        fh.seek(0)
        path_foto = os.path.join(os.getcwd(),'src','img-codigos')
        with open(os.path.join(path_foto,file_name),'wb') as f:
            f.write(fh.read())
            f.close

    @staticmethod
    def service_google(Create_Service):
        CLIENT_SECRET_FILE = os.path.join(os.getcwd(),'web','client_secret.json')
        API_NAME = 'drive'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/drive']
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        return service

if __name__=='__main__':
    #sos = Sheets()
    #sos.crear_file('Inventario_2021_07_24.xlsx',Create_Service)
    pass
    #sos = Fotos()
    #sos.create_file('DOM-BL0801.jpg',Create_Service)
    #download_file()
    #update_file()