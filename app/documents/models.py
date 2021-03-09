from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from os.path import join
from io import StringIO
import re
from nltk import ngrams

from app.db import db, BaseModelMixin
from app.common.timestamp_mixin import TimestampMixin
from config.default import UPLOAD_FOLDER


class Documents(db.Model, BaseModelMixin, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_by_name(self):
        return Documents.query.filter_by(name=self.name).first()

    def get_stats_coincidence(self):
        document_url = join(UPLOAD_FOLDER, self.url)
        text_process = self.get_text_from_pdf(document_url)
        documents_list = Documents.query.filter(
            Documents.name != self.name).all()
        result_ngram = self.get_ngram_method(text_process, documents_list)
        print(result_ngram)

    def get_ngram_method(self, doc_up, list_store_doc, n=3):
        list_ngrams_upload = list(ngrams(doc_up, n))
        list_result = []
        list_merge = []
        for doc in list_store_doc:
            docs_pro = self.get_text_from_pdf(join(UPLOAD_FOLDER, doc.url))
            doc_tgram = list(ngrams(docs_pro, n))
            common = []
            for gram in list_ngrams_upload:
                if gram in doc_tgram:
                    common.append(gram)
            if len(common) > 0:
                uniq_gram = self.remove_duplicate(common)
                total_grams = self.remove_duplicate(
                    list_ngrams_upload+doc_tgram)
                total_result = '{:.4f}'.format(
                    (len(uniq_gram)/len(total_grams))*100)
                list_result.append(
                    {"ngram": total_result, "suspect_id": doc.id, "name": doc.name})
        return list_result

    def get_text_from_pdf(self, url):
        regex = r"/\t|\n|\/|\,|\.|\:|\;|\(|\)|\{|\}|\?|\¿|\"|\'|\_|\-|\]|\[/g"
        process_text = None
        output_string = StringIO()
        with open(url, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        process_text = output_string.getvalue()
        if len(process_text) > 0:
            process_text = process_text.lower()
            process_text = re.sub(regex, "", process_text)
            process_text = re.sub(r'\d+', '', process_text)
            process_text = re.split("  *", process_text)
        return process_text

    def remove_duplicate(self, list_of_item):
        unique = list(dict.fromkeys(list_of_item))
        return unique
