from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class Security:
    _password_hasher = PasswordHasher()

    @classmethod
    def hash_password(cls, plain_password: str) -> str:
        hashed_password = cls._password_hasher.hash(plain_password)
        return hashed_password

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        try:
                return cls._password_hasher.verify(hashed_password, plain_password)
        except VerifyMismatchError:
            return False
        except Exception:
            return False