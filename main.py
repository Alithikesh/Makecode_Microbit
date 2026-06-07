def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
    record.set_sample_rate(10000, record.AudioSampleRateScope.RECORDING)
    basic.show_icon(IconNames.SMALL_SQUARE)
    record.start_recording(record.BlockingState.BLOCKING)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P0, 0)
    record.set_sample_rate(20000, record.AudioSampleRateScope.PLAYBACK)
    basic.show_leds("""
        . # . . .
        . # # . .
        . # # # .
        . # # . .
        . # . . .
        """)
    record.play_audio(record.BlockingState.BLOCKING)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    serial.write_line("" + str((record.audio_status(record.AudioStatus.PLAYING))))
basic.forever(on_forever)
