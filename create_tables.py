from app import app, db

# Configuração para criar as tabelas
with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")

# with app.app_context():
#     db.drop_all()
#     print("Tabelas excluidas com sucesso!")
