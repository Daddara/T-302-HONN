class WeatherGateway:
    NEW_DATA_CALLBACK_NAME = 'new_weather_data_callback'

    def __init__(self, data_sources: []):
        self.data_sources = data_sources
        self.new_data_listeners = []

    def register_new_data_listener(self, listener):
        """
        This method can be used to register a
        """
        # Validation check
        callback = getattr(listener, WeatherGateway.NEW_DATA_CALLBACK_NAME, None)
        if not callable(callback):
            print("Error: WeatherGateway: the submitted listener has no callback")
            return

        # Add listener
        self.new_data_listeners.append(listener)

    def get_data(self, lat, lon):
        """
        This method tries to load current weather data from the internal data_sources.
        """

        # Go through all data sources in order
        data = None
        is_new = False
        for source in self.data_sources:
            is_new = False
            data, is_new, error = source.load_data(lat, lon)

            # Test if the data request was successful
            if data is not None:
                break

            if error is not None:
                print(error)
                return

        # Test if data is valid
        if data is None:
            print("Error: WeatherGateway: every data source has failed to supply data")
            return None

        # Inform the raw data listeners if the data is new
        if is_new:
            for lister in self.new_data_listeners:
                lister.new_weather_data_callback(data)

        # Hand over to translate the data
        # No undefined behavior over here I've learned that from Rust and C so please hug me
        return data


class WeatherDataSource:
    pass
