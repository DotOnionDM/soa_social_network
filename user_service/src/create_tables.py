from user_service_impl.database import engine, Base
from user_service_impl.models.users import User

Base.metadata.create_all(bind=engine)
