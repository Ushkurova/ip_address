
import requests
from pyfiglet import Figlet
import folium
from folium.plugins import BeautifyIcon
def get_info_by_ip(ip='154.191.16.63'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)
        data={
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }
        for k,v in data.items():
            print(f'{k}: {v}')

        area = folium.Map(location=[response.get('lat'),response.get('lon')], zoom_start=20, tiles='OpenStreetMap')

        folium.CircleMarker(location=[response.get('lat'),response.get('lon')], popup='Egypt', radius=10, color='red',fill = True, fill_color = 'red').add_to(area)
        area.save(f"{response.get('query')}.html")
    except requests.exceptions.ConnectionError:
        print('please check your connection!')

def main():
    preview_text = Figlet(font= 'slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('write ip adress:\n')
    get_info_by_ip(ip)

if __name__ == '__main__':
    main()