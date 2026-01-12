import sys
import logging

class FrontendApp:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

    def run(self):
        try:
            self.logger.info('Starting frontend app')
            # application logic goes here
            self.logger.info('Frontend app started successfully')
        except Exception as e:
            self.logger.error(f'Error starting frontend app: {str(e)}')
            sys.exit(1)

if __name__ == '__main__':
    app = FrontendApp()
    app.run()