from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.60934


class ConvertMilesKmApp(App):
    output_text = StringProperty("0.0 km")

    def build(self):
        return Builder.load_file('convert_miles_km.kv')

    def convert(self, value):
        try:
            miles = float(value)
            km = miles * KM_PER_MILE
            self.output_text = f"{km:.2f} km"
        except ValueError:
            self.output_text = "0.0 km"

    def handle_increment(self, value, increment):
        try:
            miles = float(value)
        except ValueError:
            miles = 0
        miles += increment
        self.root.ids.input_miles.text = str(miles)
        self.convert(miles)


if __name__ == '__main__':
    ConvertMilesKmApp().run()