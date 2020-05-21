from Documento import Documento


cpf = 99682842115
cnpj = 17555477010603

documento_pessoal = Documento.cria_documento(cpf)
documento_empresarial = Documento.cria_documento(cnpj)
print(documento_pessoal)
print(documento_empresarial)

print(type(documento_empresarial))
