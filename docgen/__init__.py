from docxtpl import DocxTemplate

path = "../Templates/"

def replace (template, context, doc_name):
    try:
        doc = DocxTemplate(path+template+".docx")
    except:
        return "template doesn't exist"
    doc.render(context)
    doc.save(path+"created/"+doc_name+".docx")
    return 'done'

if __name__=="__main__":
    context = {'name': 'Alphalejo'}
    print (replace("Sn", context, "Alpha"))