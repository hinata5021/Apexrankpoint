from glob import glob
import tkinter

setup_window = tkinter.Tk()
setup_window.title("セットアップ")
setup_window.geometry("400x300")

txtedit = open('app/player.txt', 'w', encoding='UTF-8')
apitxt = open('app/mapi.txt', 'w', encoding='UTF-8')

#チェックボックスにチェックが入ってるかの確認
origin = tkinter.BooleanVar()
xbl = tkinter.BooleanVar()
psn = tkinter.BooleanVar()
#デフォルトの設定(PCにチェックが入っている状態)
origin.set(True)
xbl.set(False)
psn.set(False)
#チェックボックスの設定
CheckBox1 = tkinter.Checkbutton(text=u"PC", variable=origin)
CheckBox1.pack()
CheckBox2 = tkinter.Checkbutton(text=u"XboX", variable=xbl)
CheckBox2.pack()
CheckBox3 = tkinter.Checkbutton(text=u"プレステ", variable=psn)
CheckBox3.pack()

#チェックボックスのチェック状況を取得
def check(event):
    global origin
    global xbl
    global psn

plt = ""

if origin.get() == True:
    plt += "origin/"

if xbl.get() == True:
    plt += "xbl/"

if psn.get() == True:
    plt += "psn/"

tllabel = tkinter.Label(text=u'IDを入力')
tllabel.pack()
#プレイヤーIDの入力欄
PlyIDbox = tkinter.Entry()
PlyIDbox.pack()
apilabel = tkinter.Label(text=u'APIを入力')
apilabel.pack()
apiky = tkinter.Entry()
apiky.pack()


def write():
    apid = apiky.get()
    PlayerID = PlyIDbox.get()
    PlayerList = plt + PlayerID#プラットフォームとIDを変数にぶち込む
    txtedit.write(PlayerList)#変数PlayerListの値をtxtに書き込む
    apitxt.write(apid)
    apitxt.close()
    txtedit.close()#txtの編集を終わる
    setup_window.destroy()#画面を閉じる

# button1をクリックした時の処理
Button = tkinter.Button(text=u'セットアップを終わる', command = write)
Button.pack()

setup_window.mainloop()