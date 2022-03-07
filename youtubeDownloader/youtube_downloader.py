import pytube
import PySimpleGUI as sg


def download(values):
    youtube = pytube.YouTube(values['video_url'])
    if values['audio_only']:
        video = youtube.streams.filter(only_audio=True)[0]
    elif values['video_only']:
        video = youtube.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').last()
    else:
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').last()

    print('Baixando o arquivo... '
          'Aguarde o download ser finalizado')
    video.download(values['destination_folder'])
    print('Download Finalizado!')


sg.theme('Reddit')
layout = [
    [sg.Text('Insert the video URL: '), sg.Input(key='video_url')],
    [sg.Radio('Audio only', group_id='Any', key='audio_only')],
    [sg.Radio('Video only', group_id='Any', key='video_only')],
    [sg.Radio('Both', default=True, group_id='Any', key='both')],
    [sg.Text('Destination Folder: '), sg.Input(key='destination_folder'), sg.FileSaveAs('Search')],
    [sg.Button('DOWNLOAD', key='download'), sg.Button('QUIT', key='quit')],
    [sg.Output(size=(70, 5))]
]

window = sg.Window('Youtube Downloader', layout, auto_size_text=True)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED or events == 'quit':
        break
    elif events == 'download':
        download(values)
