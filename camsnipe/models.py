"""
Core data models

RawListing
NormalizedListing
ScoredListing
"""

from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel Field, HttpUrl

#-------------------------------------------------------------------
# Enums 
#-----------------------------------------------------------------

class ConditionGrade(str, Enum):



class ListingSource(str, Enum):


#======== 1 Raw listing 
# Collector output
# AKA Raw listing

class RawListing(BaseModel, frozen=True):


# ======== 2 Normalized Listing (output)

class NormalizedListing(BaseModel, frozen=True):



# Valuation Result (Valuator output)

class ValuationResult(BaseModel, frozen=True):


#================3 Scored Listing - scorer output final pipeline 

class ScoredListing(BaseModel, frozen=True):




