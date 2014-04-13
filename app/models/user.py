from . import Base

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	username = Column(String(30), nullable = False)

	def __repr__(self):
		return "<User('%s')>" % self.username