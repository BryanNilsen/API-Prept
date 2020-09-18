"""
    This module makes all view classes available as a package
"""
from .profile import ProfileViewSet
from .profile import ProfileDataViewSet
from .user import UserViewSet
from .food import FoodViewSet
from .water import WaterViewSet
from .member import MemberViewSet
from .register import register_user
from .register import login_user
