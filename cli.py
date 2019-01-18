import click


'''コマンドグループ
'''
@click.group(help='[Help text]')
def cli():
    pass

@cli.command(help='AWS Transcribe')
def aws_avs():
    print('aws_avs')

@cli.command(help='Alexa Voice Service (AVS)')
def aws_transcribe():
    print('aws_transcribe')

@cli.command(help='Google Cloud Speech-to-Text')
def azure_speech():
    print('azure_speech')

@cli.command(help='Google Assistant SDK for devices')
def google_assistant():
    print('google_assistant')

@cli.command(help='Azure Speech to Text')
def google_speech():
    print('google_speech')


if __name__ == '__main__':
    cli()
