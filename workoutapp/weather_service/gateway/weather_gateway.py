class WeatherGateway:
    RAW_DATA_CALLBACK_NAME = 'raw_data_lister_callback'

    def __int__(self, data_sources):
        self.data_sources = data_sources
        self.raw_data_listeners = []

    def register_raw_data_listener(self, listener):
        """
        This method can be used to register a
        """
        # Validation check
        callback = getattr(listener, WeatherGateway.RAW_DATA_CALLBACK_NAME, None)
        if not callable(callback):
            print("Error: WeatherGateway: the submitted listener has no callback")
            return

        # Add listener
        self.raw_data_listeners.append(listener)

    def get_data(self, city):
        """
        This method tries to load current weather data from the internal data_sources.
        """

        # Go through all data sources in order
        data = None
        is_new = False
        for source in self.data_sources:
            is_new = False
            data, is_new = source.load_data(city)

            # Test if the data request was successful
            if data is not None:
                break

        # Test if data is valid
        if data is None:
            print("Error: WeatherGateway: every data source has failed to supply data")
            return None

        # Inform the raw data listeners if the data is new
        if is_new:
            for lister in self.raw_data_listeners:
                lister.raw_data_lister_callback(data)

        # Hand over to translate the data
        # No undefined behavior over here I've learned that from Rust and C so please hug me
        return self._translate_raw_data(data)

    def _translate_raw_data(self, data):
        return None


class WeatherDataSource:
    pass
