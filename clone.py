import os
import sys
from colorama import Fore
import time
import random
arllll = random.randint(1,999)
alssss = random.randint(1,999)
asmlll = random.randint(1,999)
alsss = random.randint(1,999)
lua = input("Chat:")
if lua =='kick':
	yu = input("Vui lòng nhập tên đối tượng bị band:")
	ys = input("Vui lòng nhập lí do bị band:")
	print(Fore.RED + "Hệ thống:người dùng " + yu + " đã bị band vì lí do:" + ys)
	os.system("python clone.py")
elif lua =="":
	print("Câu lệnh không hợp lệ vui lòng thử lại")
	os.system("python clone.py")
elif lua =='bot:check':
	print("🌺Tran trung xam lon deo ben em🌺"*1000)
	print('\n')
	os.system("python clone.py")
elif lua =='member:info':
	asm = random.randint(5,80)
	print(Fore.YELLOW + "Số thành viên là:", asm)
	os.system("python clone.py")
elif lua =='bypass:keyinfo':
	print(Fore.BLUE + "Vui lòng đợi FustKing trích dữ liệu key")
	time.sleep(5)
	ass = 'Key:Aliec xem xiếc( </> ) Phát hiện người dùng ăn cắp dữ liệu member!'
	print(Fore.YELLOW + ass)
	os.system("python clone.py")
elif lua =='bypass:back-vession':
	print(Fore.CYAN + "FustKing </> Đang trích xuốt dữ liệu botchat vession 0.5")
	time.sleep(3)
	print("< / > https://github.com/KHANHNROLAU/BOT")
	os.system("python clone.py")
elif lua =='bot:reset':
	os.system("python mess.py")
elif lua =='set':
	print("Vui lòng chọn loại set:")
	print("1.Set love\n2.Set name\n3.Setup")
	lop = input("Set:")
	if lop =='1':
		mine =input('Vui lòng chọn member bị bắt buộc setlove:')
		print(Fore.MAGENTA + "Admin đã setup với",mine)
		os.system("python clone.py")
	elif lop =='2':
		setul = input("Vui lòng chọn id đối tượng:")
		setnam = input("Vui lòng chọn member để set lại name:")
		print(Fore.BLUE + "Hệ thống:phát hiện tên người dùng có id là",setul + " có hành vi đặt id trái quy định server cho phép nên hệ thống sẽ đổi thành:",setnam)
		os.system("python clone.py")
	elif lop =='3':
		print("Bạn đã được setup rồi không cần setup nữa!")
		os.system("python clone.py")
elif lua =='add':
	print(Fore.YELLOW + "1.Add member(Ảo)\n2.Add Bot(Ảo)\n3.Add Rule(Chỉnh ở file)")
	lien = input("Command:")
	if lien =='1':
		likk = input("Nhập tên member cần add:")
		print(Fore.WHITE + "Người dùng ",likk +" Đã được thêm vào server")
		os.system("python clone.py")
	elif lien =='2':
		liks = input("Nhập tên bot cần add:")
		likss = input("Nội dung muốn add:")
		print(Fore.YELLOW + "Bot ",liks + " đã được thêm vào server vì: ",likss)
		os.system("python clone.py")
	elif lien =='3':
		print("Ví dụ:rlik = input('command:')")
		rikl = input("Nhập hàm input:")
		print(Fore.YELLOW + "Ví dụ:rlik = input('command:') thì Nhập câu đầu:rlik")
		rlksd = input("Nhập câu đầu:")
		print(Fore.YELLOW + "Ví dụ:Nhập câu lệnh muốn chat thì ghi là 'vonek'")
		rikc = input("Nhập câu lệnh muốn chat rule:")
		riks = input("Nhập code để câu lệnh được áp dụng:")
		print(Fore.YELLOW + "Câu lệnh bạn là:")
		print(Fore.YELLOW + rikl)
		print("if", rlksd + "==" + rikc + ":")
		print("	", riks)
		os.system("python clone.py")
elif lua =='rule':
	print("Player rule -admin | rule:No Root")
	os.system("python clone.py")
elif lua =='root/=rule.admin':
	os.system("clear")
	print(Fore.RED + "Warting!") 
	usa = input("Key để truy cập nhà phát triển:")
	if usa !='12345':
		print("Bạn không phải nhà phát triển!")
		time.sleep(3)
		os.system("python mess.py")
	else:
		print("Truy cập thành công")
		time.sleep(1)
	os.system("clear")
	print(Fore.YELLOW + "</>")
	print("Command Dev:\n1.Close\n2.On Warting\n3.Delete Server")
	rt = input("Command:")
	if rt =='1':
		os.system("python mess.py")
	elif rt =='2':
		print(Fore.YELLOW + "Online Warting Sau 3 giây")
		time.sleep(2)
		os.system("clear")
		print(Fore.RED + "3")
		time.sleep(1)
		print(Fore.RED  + "2")
		time.sleep(1)
		print(Fore.RED + "1")
		time.sleep(1)
		os.system("clear")
		alin = '''Welcome to Dev

Communities: https://termux.org/community
Gitter chat: https://gitter.im/termux/termux
IRC channel: #termux on libera.chat

Working with packages:

 * Search packages:   pkg search <query>
 * Install a package: pkg install <package>
 * Upgrade packages:  pkg upgrade

Subscribing to additional repositories:

 * Root:     pkg install root-repo
 * X11:      pkg install x11-repo

Report issues at https://termux.org/issues

'''
		print(alin)
		rtm = input("~ $ ")
		print("Chỉ để ngắm thôi")
		time.sleep(3)
		os.system("python mess.py")
	elif rt =='3':
		os.remove("mess.py")
		os.remove("clone.py")
		os.remove("Loinhac.txt")
		quit()
elif lua =='bot:spam':
	print(Fore.BLUE + "Chọn mức ngưỡng spam:")
	print(Fore.YELLOW + "1.10\n2.50\n3.100\n4.200\n5.500\n6.800\n7.1000\n8.4000\n9.8000\n10.10000")
	lip = input("Command:")
	if lip =='1':
		print(Fore.CYAN + "Tips:Nên ghi là: Địt con mẹ em ")
		nmal = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + nmal*10)
		os.system("python clone.py")
	elif lip =='2':
		print(Fore.BLUE + "Tips:Nên ghi là: Địt con mẹ em ")
		condiv = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + condiv*50)
		os.system("python clone.py")
	elif lip =='3':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		linx = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + linx*100)
		os.system("python clone.py")
	elif lip =='4':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		linxm = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + linxm*200)
		os.system("python clone.py")
	elif lip =='5':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		rmsl = input("Command cần spam:")
		print(Fore.CYAN + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + rmsl*500)
		os.system("python clone.py")
	elif lip =='6':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		dcmad = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + dcmad*800)
		os.system("python clone.py")
	elif lip =='7':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		livvm = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + livvm*1000)
		os.system("python clone.py")
	elif lip =='8':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		links = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + links*4000)
		os.system("python clone.py")
	elif lip =='9':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		linksd = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + linksd*8000)
		os.system("python clone.py")
	elif lip =='10':
		print(Fore.YELLOW + "Tips:Nên ghi là: Địt con mẹ em ")
		sexyvl = input("Command cần spam:")
		print(Fore.YELLOW + "Bot đang viết spam...")
		time.sleep(1.5)
		print(Fore.YELLOW + sexyvl*10000)
		os.system("python clone.py")
elif lua =='bot:delete-cache':
	print("Cache là Loinhac.txt")
	print("Bạn có chắc chắn xóa?")
	ipa = input("Y/N:")
	if ipa =='Y':
		os.remove("Loinhac.txt")
		print("xóa thành công")
		os.system("python clone.py")
	elif ipa =='y':
		os.remove("Loinhac.txt")
		print("Xóa thành công!")
		os.system("python clone.py")
	elif ipa =='N':
		os.system("python clone.py")
	elif ipa =='n':
		os.system("python clone.py")
elif lua =='bot:check-vession':
	print("Vession bot là 0.9")
	os.system("python clone.py")
elif lua =='bot:random':
	asml = random.randint(1,99999999999999999)
	print(asml)
	os.system("python clone.py")
elif lua =='bot:help':
	print(Fore.YELLOW + "[ Full command ]")
	print(Fore.BLUE + "[1.bot:reset] | [2.bot:bot:spam]")
	print(Fore.CYAN + "[3.bot:delete-cache] | [4.bot:check-vession]")
	print(Fore.CYAN  + "[5.bot:random] | [6.bot:box]")
	print(Fore.YELLOW + "[7.bot:name-server]")
	os.system("python clone.py")
elif lua =='bot:box':
	print(Fore.YELLOW + "box:chat để xem")
	os.system("pythin clone.py")
elif lua =='guide':
	print(Fore.YELLOW + "Hướng dẫn tân thủ")
	print(Fore.BLUE + "kick:Dùng để kick người dùng ssh")
	print(Fore.CYAN + "rule:Check rule Player")
	print(Fore.GREEN + "member:info = kiểm tra số người dùng ssh")
	print(Fore.BLUE + "bot:help = kiểm tra command")
	print(Fore.YELLOW + "set:Dùng đi rồi bt")
	print(Fore.YELLOW + "add:dùng ik hay lắm")
	os.system("python clone.py")
elif lua =='bot:name-server':
	print(Fore.BLUE + "Name Server:Box-Chat5263")
	os.system("python clone.py")
elif lua =='bypass:random':
	asmrsex = random.randint(1,99999999999999)
	print(Fore.BLUE + "Bot đang viết số random...")
	time.sleep(2)
	print(Fore.YELLOW + "Số bạn random ra là:")
	print(asmrsex)
	os.system("python clone.py")
elif lua =='bypass:create-login':
	os.system("clear")
	checkk = input("Username:")
	if checkk !='bypass:show.login':
		quit()
	else:
		print("username:fusking | Password:12345")
	ritprox = input("Email:")
	if ritprox !='fusking':
		quit()
	else:
		print(Fore.YELLOW + "Bypass email succes")
	passwordsiu = input("Password:")
	if passwordsiu !='12345':
		quit()
	else:
		print("Login succes")
		time.sleep(2)
		print("1")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("3")
		time.sleep(1)
		os.system("python mess.py")
elif lua =='bypass:exit':
	print(Fore.BLUE + "Đang thoát...")
	time.sleep(2)
	quit()
elif lua =='bypass:game':
	print(Fore.YELLOW + "1.Tài xỉu")
	print(Fore.YELLOW + "2.Gacha")
	print(Fore.YELLOW + "3.Random")
	print(Fore.YELLOW + "4.Kéo Búa Bao")
	iposmin = input("Command:")
	if iposmin =='1':
		print(Fore.BLUE + "1.Tài(Dùng đc)\n2.Xỉu(Lỗi)")
		rtplu = input("Lựa chọn:")
		if rtplu =='1':
			print("Nhà cái đang xác định...")
			time.sleep(3)
			if asmlll>alsss:
				print("Tài thắng")
				print("Xỉu thua")
				os.system("python clone.py")
			if alsss>asmlll:
				print("Xỉu thắng")
				print("Tài thua")
				os.system("python clone.py")
	elif iposmin =='2':
		print(Fore.YELLOW + "1.Go")
		print(Fore.YELLOW + "2.Out")
		rtupoo = input("Lựa chọn:")
		if rtupoo =='1':
			print(Fore.BLUE + "Đang xác định quà!")
			time.sleep(3)
			print("</>...")
			time.sleep(2)
			os.system("clear")
			time.sleep(2)
			print("1.Đồ chơi dã thú")
			print("2.Cây gậy màu tím")
			amsssllc = random.randint(9,10)
			amssjlf = random.randint(1,10)
			print(Fore.YELLOW + "</> đang bắt đầu quay...")
			time.sleep(2)
			if amsssllc>amssjlf:
				print("Chúc mừng bạn chúng đồ chơi dã thú")
				os.system("python clone.py")
			else:
				print("Chúc mừng bạn chúng cây gậy màu tím")
				os.system("python clone.py")
	elif iposmin =='3':
		assssll = random.randint(1,99909080)
		print(Fore.BLUE + "Số random bạn là:")
		print(Fore.BLUE  +str(assssll))
		os.system("python clone.py")
	elif iposmin =='4':
		print(Fore.CYAN + "1.Kéo")
		print(Fore.CYAN + "2.Búa")
		print(Fore.CYAN + "3.Bao")
		liness = input("Lựa chọn:")
		alscmd = random.randint(1,300)
		alscms = random.randint(1,300)
		if liness =='1':
			if alscmd>alscms:
				print("Kéo thua")
				os.system("python clone.py")
			else:
				print("Kéo thắng")
				os.system("python clone.py")
		elif liness =='2':
				if alscmd>alscms:
					print("Búa thắng")
					os.system("python clone.py")
				else:
					print("Búa thua")
					os.system("python clone.py")
		elif liness =='3':
			if alscmd>alscms:
				print("Bao thua")
				os.system("python clone.py")
			else:
				print("Búa thắng")
				os.system("python clone.py")
elif lua =='bypass:exit':
	quit()
elif lua =='bypass:close-menu':
	os.system("clear")
	print("Close menu thành công")
	os.system("python clone.py")
elif lua =='bypass:shop':
	print(Fore.YELLOW + "Khu shop help shop bằng câu lệnh bypass:shop dùng để tra thông tin những câu lệnh liên quan đến có đuôi shop\n1.bypass:shop:buy: dùng để xem những thứ được rao bán trên màn hình hệ thống và mỗi vật phẩm sẽ có @id riêng\n2.bypass:shop:buy:@id bạn có thể mua không giới hạn vì đây là server botchat lậu")
	os.system("python clone.py")
elif lua =='bypass:html-crash-termis':
	amakindlo = input("Website cần bị crash:")
	aninesssla = amakindlo
	rule34dam = requests.get(aninesssla)
	html_content = rule34dam.text
	
	print(html_content)
	os.system("python clone.py")
elif lua =='bypass:download-jpg':
	anhcanina = input("Link cần install ảnh gái thông qua python:")
	namechogai = input("Tên file cần lưu ảnh:")
	print("Xin vui lòng đợi bot đang lên google và dán thông tin bạn vừa đưa ra </>")
	time.sleep(2)
	urlanhgaisac = anhcanina
	with open(anhcaninai, "wb") as sexminevle:
		sexminevle.write(requests.get(namechogai).content)
	print(Fore.YELLOW + "Install succes")
	os.system("python clone.py")