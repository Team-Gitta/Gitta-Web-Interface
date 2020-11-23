import qrcode

def makeQRcode(input_data):
    # example data
    data = input_data
    # output file name
    filename = "qrcode.png"
    # generate qr code
    img = qrcode.make(data)
    # save img to a file
    img.save('static/images/qrcode.png')
    print("complete")
