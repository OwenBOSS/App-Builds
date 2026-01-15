import webview

class BeamAPI:
    def calculate_beam(self, data):
        # Extract inputs from JS (units: meters, kN, etc.)
        span = float(data['span'])
        load = float(data['load'])
        
        # Simple structural logic: Max Moment = (w * L^2) / 8
        max_moment = (load * (span ** 2)) / 8
        max_shear = (load * span) / 2
        
        return {
            'moment': round(max_moment, 2),
            'shear': round(max_shear, 2),
            'status': "Success"
        }

api = BeamAPI()
window = webview.create_window('Beam Designer', 'index.html', js_api=api)
webview.start()
