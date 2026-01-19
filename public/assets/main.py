import sys
import logging
from logging.handlers import RotatingFileHandler

class FrontendApp:
    def __init__(self, log_level=logging.INFO, log_file='frontend_app.log', max_log_size=10*1024*1024, backup_count=5):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)
        self.file_handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
        self.file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.file_handler)

    def run(self):
        try:
            self.logger.info('Starting frontend app')
            # application logic goes here
            self.logger.info('Frontend app started successfully')
        except Exception as e:
            self.logger.error(f'Error starting frontend app: {str(e)}', exc_info=True)
            sys.exit(1)

    def stop(self):
        self.logger.info('Stopping frontend app')
        self.logger.removeHandler(self.handler)
        self.logger.removeHandler(self.file_handler)
        self.logger = None

if __name__ == '__main__':
    try:
        app = FrontendApp()
        app.run()
    except KeyboardInterrupt:
        if 'app' in locals():
            app.stop()
        sys.exit(0)
    except Exception as e:
        print(f'Error: {str(e)}')
        sys.exit(1)