class CPU():

    _model: str

    def __init__(self, model: str):
        self._model = model

    @property
    def model(self):
        return self._model
