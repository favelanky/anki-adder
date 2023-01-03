from win10toast import ToastNotifier


def notify(sentence, trans, syn):
    toaster = ToastNotifier()
    text_trans = ''
    for i in trans[0]:
        text_trans += i + ', '
    toaster.show_toast(f"{sentence}", f"{text_trans}", duration=20)
