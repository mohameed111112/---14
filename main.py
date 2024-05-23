basic.show_string("mohammed")
def on_button_pressed_a():
    basic.show_icon(IconNames.heart)
    def on_button_pressed_b():
        global z
        z += 1
        basic.show_number(z)
        input.on_button_pressed(button.b,  on_button_pressed_b)
        def on_gesture_shake():
            pass
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        for i in range(6):
            basic.show_number(i) 
            input.on_gesture(gesture.shake, on_gesture_shake)
            sum=40
            def on_button_pressed_ab():
                global sum 
                if sum >= 50:
                    basic.show_string("pass")
                    else:
                        basic.show_String("fall")
                        input.on_button_pressed(button.ab, on_button_pressed_ab)

