from passlib.hash import sha256_crypt


def encrypt_field(field: str):
  return sha256_crypt.encrypt(field)


def compare_field(db_value: str, field: str):
  return sha256_crypt.verify(field, db_value)
