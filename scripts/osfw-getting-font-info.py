#!/usr/bin/python
# -*- coding: UTF-8 -i*-
# This is script for getting font information from ttf file and
# adding it to database
#
# Permission is hereby granted, without written agreement and without
# license or royalty fees, to use, copy, modify, and distribute this
# software and its documentation for any purpose, provided that the
# above copyright notice and the following two paragraphs appear in
# all copies of this software.
#
# IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES
# ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN
# IF THE COPYRIGHT HOLDER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
#
# THE COPYRIGHT HOLDER SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE PROVIDED HEREUNDER IS
# ON AN "AS IS" BASIS, AND THE COPYRIGHT HOLDER HAS NO OBLIGATION TO
# PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
#
# Red Hat Author(s): Pravin Satpute <psatpute@redhat.com>
#/


import os, sys
import sqlite3

imagestr = {
#todo add more script tag
# Not found script tag in these fonts, need to check whether these fonts required script tag or not NotoSansCarian, NotoSansDeseret, NotoSansEgyptianHieroglyphsE, NotoSansGlagolitic, NotoSansImperialAramaic, NotoSansLisu, NotoSansLycian, NotoSansLydian, NotoSansOldSouthArabian, NotoSansOldTurkic, NotoSansOsmanya, NotoSansPhoenician, NotoSansShavian, NotoSansSymbols, NotoSansUgaritic, NotoSansVai
		"deva":"मी काच खाऊ शकतो, मला ते दुखत नाही.",
		"beng":"আমি কাঁচ খেতে পারি, তাতে আমার কোনো ক্ষতি হয় না।",
		"gujr":"હું કાચ ખાઇ શકુ છુ અને તેનાથી મને દર્દ નથી થતુ.",
		"knda":"ನಾನು ಗಾಜನ್ನು ತಿನ್ನಬಲ್ಲೆ ಮತ್ತು ಅದರಿಂದ ನನಗೆ ನೋವಾಗುವುದಿಲ್ಲ.",
		"mlym":"വേദനയില്ലാതെ കുപ്പിചില്ലു് എനിയ്ക്കു് കഴിയ്ക്കാം.",
		"orya":"ମୁଁ କାଚ ଖାଇପାରେ ଏବଂ ତାହା ମୋର କ୍ଷତି କରିନଥାଏ।.",
		"guru":"ਮੈਂ ਗਲਾਸ ਖਾ ਸਕਦਾ ਹਾਂ ਅਤੇ ਇਸ ਨਾਲ ਮੈਨੂੰ ਕੋਈ ਤਕਲੀਫ ਨਹੀਂ.",
		"taml":"நான் கண்ணாடி சாப்பிடுவேன், அதனால் எனக்கு ஒரு கேடும் வராது.",
		"telu":"నేను గాజు తినగలను అయినా నాకు యేమీ కాదు.",
		"arab":"میں کانچ کھا سکتا ہوں اور مجھے تکلیف نہیں ہوتی ۔",
		"armn":"Կրնամ ապակի ուտել և ինծի անհանգիստ չըներ",
		"geor":"მინას ვჭამ და არა მტკივა.",
		"thai": "เป็นมนุษย์สุดประเสริฐเลิศคุณค่า - กว่าบรรดาฝูงสัตว์เดรัจฉาน",
		"hebr": "דג סקרן שט לו בים זך אך לפתע פגש חבורה נחמדה שצצה כך.",		
		"brah":"𑀓𑀔𑀕𑀖𑀗𑀘𑀙𑀚𑀛𑀜𑀝𑀞𑀟𑀠𑀡",
		"cher":"ᎧᎨᎩᎪᎫᎬᎭᎮᎯᎰᎱᎲᎳᎴᎵᎶᎷᎸ",
		"copt":"ϢϣϤϥϦϧϨϩϪϫϬϭϮϯⲀⲁⲂⲃⲄⲅ",
		"hano":"ᜣᜤᜥᜦᜧᜨᜩᜪᜫᜬᜭᜮᜯᜰᜱ",
		"kthi":"𑂍𑂎𑂏𑂐𑂑𑂒𑂓𑂔𑂕𑂖𑂗𑂘𑂙𑂛𑂝𑂞𑂟𑂠𑂡𑂢",
		"kali":"꤀꤁꤂꤃꤄꤅꤆꤇꤈꤉ꤊꤋꤌꤍꤡ",
		"khar":"𐨨𐨐𐨕𐨑𐨡𐨭𐨐𐨟𐨨𐨫𐨟𐨡𐨑𐨟𐨣𐨱",
		"khmr":"មកជខវឝកទមលតដខតនហ",
		"lao":"ກຂຄງຈຊຍດຕຖທນບປຜ",
		"mand":"ࡁࡂࡃࡄࡅࡆࡇࡈࡉࡊࡋࡌࡍࡎࡏ",
		"mtei":"ꯀꯈꯒꯘꯉꯆꫢꯖꯓꫣꫤꫥꫦꫧꫨ",
		"nko":"߀߁߂߃߄߅߆߇߈߉ߊߍߋߐߏ",
		"tglg":"ᜁᜂᜃᜄᜅᜆᜇᜈᜉᜊᜋᜌᜎᜏᜐ",
		"cyrl":"Чешће цeђење мрeжастим џаком побољшава фертилизацију генских хибрида.",
		"grek":"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)",
		"hani":"いろはにほへと ちりぬるを 色は匂へど 散りぬるを",
		"tibt":"ཤེལ་སྒོ་ཟ་ནས་ང་ན་གི་མ་རེད།",
}

def get_viewstr(scriptsupport):
	viewstr = "NULL"
#	print "before loop", viewstr

	if scriptsupport[0].find("dev") >=1:
		viewstr = imagestr["deva"]
#		print "in deva"
	elif scriptsupport[0].find("ben") >=1:
#		print "in beng"
		viewstr = imagestr["beng"]
	elif scriptsupport[0].find("guj")>=1:
#		print "in gujr"
		viewstr = imagestr["gujr"]
	elif scriptsupport[0].find("knd")>=1:
#		print "in knda"
		viewstr = imagestr["knda"]
	elif scriptsupport[0].find("mly")>=1:
#		print "in mlym"
		viewstr = imagestr["mlym"]
	elif scriptsupport[0].find("ory")>=1:
#		print "in orya"
		viewstr = imagestr["orya"]
	elif scriptsupport[0].find("gur")>=1:
#		print "in guru"
		viewstr = imagestr["guru"]
	elif scriptsupport[0].find("tam")>=1:
#		print "in taml"
		viewstr = imagestr["taml"]
	elif scriptsupport[0].find("tel") >=1:
#		print "in telu"
		viewstr = imagestr["telu"]
	elif scriptsupport[0].find("ara") >=1:
		viewstr = imagestr["arab"]
#		print "in arab"
	elif scriptsupport[0].find("armn") >=1:
		viewstr = imagestr["armn"]
#		print " in armn"
	elif scriptsupport[0].find("geor") >=1:
		viewstr = imagestr["geor"]
#		print " in geor"
	elif scriptsupport[0].find("thai") >=1:
		viewstr = imagestr["thai"]
#		print " in thai"	
	elif scriptsupport[0].find("hebr") >=1:
		viewstr = imagestr["hebr"]
#		print " in hebr"
	elif scriptsupport[0].find("brah") >=1:
		viewstr = imagestr["brah"]

	elif scriptsupport[0].find("cher") >=1:
		viewstr = imagestr["cher"]

	elif scriptsupport[0].find("copt") >=1:
		viewstr = imagestr["copt"]

	elif scriptsupport[0].find("hano") >=1:
		viewstr = imagestr["hano"]

	elif scriptsupport[0].find("kthi") >=1:
		viewstr = imagestr["kthi"]

	elif scriptsupport[0].find("kali") >=1:
		viewstr = imagestr["kali"]

	elif scriptsupport[0].find("khar") >=1:
		viewstr = imagestr["khar"]

	elif scriptsupport[0].find("khmr") >=1:
		viewstr = imagestr["khmr"]

	elif scriptsupport[0].find("lao") >=1:
		viewstr = imagestr["lao"]

	elif scriptsupport[0].find("mand") >=1:
		viewstr = imagestr["mand"]

	elif scriptsupport[0].find("mtei") >=1:
		viewstr = imagestr["mtei"]
	elif scriptsupport[0].find("nko") >=1:
		viewstr = imagestr["nko"]

	elif scriptsupport[0].find("tglg") >=1:
		viewstr = imagestr["tglg"]

	elif scriptsupport[0].find("hani") >=1:
		viewstr = imagestr["hani"]
	elif scriptsupport[0].find("tibt") >=1:
		viewstr = imagestr["tibt"]


	if viewstr == "NULL":
		viewstr = "The quick brown fox jumps over the lazy dog"
	return viewstr

def process_file(filename):
        ipfile = open(filename)
        flines = ipfile.readlines()
	matching = [s for s in flines if "family:" in s]
	print matching
	global FamilyName
#	FamilyName = matching[0][10:-5]
#	print "Family name:\t", family
#	matching = [s for s in flines if "file:" in s]
#	ttfilename = matching[0][8:-5]
#	fileName = os.path.basename(ttfilename)
	matching = [s for s in flines if "\tlang:" in s]
	global LangSupport
	LangSupport = " "+ matching[0][7:-4] + " "
	LangSupport = LangSupport.replace('|',' ')
	print LangSupport
#	print "Languages Supported:\t", LangSupport
	matching = [s for s in flines if "fontformat:" in s]
	global FontFormat
	FontFormat =  matching[0][14:-5] 
#	print "Font format:\t", FontFormat
	global Scripttags
	Scripttags = ""
	scriptsupport = [s for s in flines if "capability:" in s]
	if len(scriptsupport) == 0:
		Scripttags = "latn"
		viewstr = "The quick brown fox jumps over the lazy dog"
	else:
		scriptsupportstring = scriptsupport[0].replace(':',' ').replace('"',' ').split()
		for word in scriptsupportstring:
			if len(word)==4:
				Scripttags = Scripttags + word + ", "
		viewstr = get_viewstr(scriptsupport)
	print Scripttags
	

#	print "viewstr_funct", viewstr

        global ViewString
        ViewString = viewstr

#generate waterfall, sample and pdf for fonts
#        gen_wimage =  'pango-view --font=' + ttfilename + ' --text \"' + viewstr + '\" --hinting auto --waterfall -o ' + fileName[0:-4] + '.png  -q' 
#        gen_simage =  'pango-view --font ' + ttfilename + ' --text \"' + viewstr + '\" --hinting auto -o ' + fileName[0:-4] + "-sample" + '.png  -q' 
#	gen_spdf = 'fntsample -f ' +  ttfilename +  ' -o ' + fileName[0:-4]+ '.pdf'
#	os.system(gen_wimage)
#	os.system(gen_simage)
#	os.system(gen_spdf)

def process_otfinfo(filename):
        ipfile = open(filename)
        flines = ipfile.readlines()
	matching = [s for s in flines if "Version:" in s]
	global Version
	words = matching[0].split("Version:")
	print words
#	for word in words:
	Version = words[1].replace("  ", "").replace("\n","").replace(" Version","")
	matching = [s for s in flines if "Subfamily:" in s]
	words = matching[0].split()
	global SubFamily
	SubFamily = words[1]
	matching = [s for s in flines if "Family:" in s]
	global FamilyName
	words = matching[0].split("Family:")
	FamilyName = words[1].replace("  ","").replace("\n","")

def process_rpmquery(filename):
        ipfile = open(filename)
#	print "processig file" + filename
        flines = ipfile.readlines()
	licenseline = [s for s in flines if "License" in s]
	licenseline = licenseline[0]
	words = licenseline.split()
	global License
	License = words[2]
#	print "license:", words[2]
	urlline = [s for s in flines if "URL" in s]
	urlline = urlline[0]
	words = urlline.split()
	global UpstreamUrl
	UpstreamUrl = words[2]
	k = 0
	print "len of fline", len(flines)
	for s in flines:
		k = k +1
		if "Description" in s:
			print "fount description", s
			break
#	print k
#	print "length of", len(flines)
	li = ""
	for x in range(k, len(flines)):
		print flines[x]
		li = li + flines[x]
	global Description
	li = li.replace("\n", " ")
	Description = li
#	print li
#	print "type of li", type(li)
			
#	description = [s for s in flines if "Description" in s]
#	print "descrption:", description
#	print type(description)
#	print "upstream url:",words[2]

def process_fontaininfo(filename):
        ipfile = open(filename)
        flines = ipfile.readlines()
	global Copyright
	copyrightline = [s for s in flines if "Copyright" in s]
	if len(copyrightline) == 0:
		Copyright = "FIXME"
#		print Copyright
	else:
		words = copyrightline[0].split('t: ')
		Copyright = words[1]

	global GlyphCount
	glyphcountline = [s for s in flines if "Glyph" in s]
        words = glyphcountline[0].split()
	GlyphCount = int(words[2])

	global CharacterCount
	charactercountline = [s for s in flines if "Character" in s]
	words = charactercountline[0].split()
	CharacterCount = int(words[2])


if __name__ == "__main__":
	global fontname, FamilyName, SubFamilyName, TtfName, Version, LangSupport, Scripttags, License,  Copyright, UpstreamUrl,  FontFormat, GlyphCount, CharacterCount, Description
	fontname = sys.argv[1]
	vals = []

# get info from fc-scan
	os.system("fc-scan" + " " + fontname + ">" + " "+ "out" )
        process_file("out")
	os.system("rm -rf" + " out" )	

# get upstream url from rpmquery
	rpmquery = "rpm -qf " + fontname + " > rpmnamefile "
	os.system(rpmquery)
        ipfile = open("rpmnamefile")
	fline = ipfile.readlines()
	rpmname = fline[0][:-1]
	rpmqi = "rpm -qi " + rpmname + " > out_rpmqi "
	os.system(rpmqi)
	process_rpmquery("out_rpmqi")
	os.system("rm -rf" + " out_rpmqi" )	

# get info from otfinfo
	os.system("otfinfo -i" + " " + fontname + ">" + " "+ "out" )
	process_otfinfo("out")
	os.system("rm -rf" + " out" )
	os.system("fontaine -T -r -f" + " " + fontname + ">" + " "+ "out" )
	process_fontaininfo("out")
	TtfName = os.path.basename(fontname)
	print TtfName
	print FamilyName
	print SubFamily
        print Description
	print "Version:", Version
	print License
	print UpstreamUrl
	print LangSupport
	print Scripttags
	print Copyright
	print FontFormat
	print ViewString
	ViewString = ViewString.decode("utf8")
	Like = 0
	Woffurl = "FIXME"
        vals = [(FamilyName, Description, SubFamily, Version, License, UpstreamUrl, LangSupport, Scripttags, TtfName, FontFormat, Copyright, ViewString, GlyphCount, CharacterCount, Woffurl, Like )]
	print vals
        sqlite3.connect
#        db1  = sqlite3.connect("storage.db")
#        db1  = sqlite3.connect("sqlite3.db")
#        curs = db1.cursor()
#        stmt = "insert into osfw_osfw (familyname,description, subfamily, version, license, upstreamurl, langsupport, scriptsupport, ttffilename, fontformat, copyright, viewstring, glyphcount, charactercount, woffurl, likes) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#        curs.executemany(stmt, vals)
#	db1.commit()
#	db1.close()

# Generating images
	ViewString  = ViewString.encode("utf8")
        gen_wimage =  'pango-view --font=\"' + FamilyName + " " + SubFamily + '\" --text \"' + ViewString + '\" --hinting auto --waterfall -o ' + TtfName[0:-4] + '.png  -q' 
	print gen_wimage
        gen_simage =  'pango-view --font=\"' + FamilyName + " " + SubFamily + '\" --text \"' + ViewString + '\" --hinting auto -o ' + TtfName[0:-4] + "-sample" + '.png  -q' 
	print gen_simage
	gen_spdf = 'fntsample -f ' +  fontname +  ' -o ' + TtfName[0:-4]+ '.pdf'
	os.system(gen_wimage)
	os.system(gen_simage)
	os.system(gen_spdf)

