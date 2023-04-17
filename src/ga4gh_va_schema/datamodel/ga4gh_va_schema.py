# Auto generated from ga4gh_va_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-17T13:44:03
# Schema: GA4GH-VA-Core-IM
#
# id: https://w3id.org/ga4gh-va-core-im
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, String
from linkml_runtime.utils.metamodelcore import Bool, string

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CAM = CurieNamespace('CAM', 'http://example.org/CAM/')
DC = CurieNamespace('DC', 'https://example.com/dc')
FHIR = CurieNamespace('FHIR', 'http://example.org/FHIR/')
FRBR = CurieNamespace('FRBR', 'https://vocab.org/frbr/core')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PROV = CurieNamespace('PROV', 'http://www.w3.org/ns/prov#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
VACOREIM = CurieNamespace('vacoreim', 'https://example.org/vacoreim/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = VACOREIM


# Types
class Url(string):
    """ A string representing a Uniform Resource Locator (RFC 1738), specifying a web address where a resource can be found or information about the resource discovered. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Url"
    type_model_uri = VACOREIM.Url


class Class(string):
    """ A string representing a class in a VA model used to type an object in the data. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Class"
    type_model_uri = VACOREIM.Class


class DateTime(string):
    """ A string value that specifies a date and time of day comprised of a year, month, day, hour, minute, and second, following the form “YYYY-MM-DDThh:mm:ss” """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "DateTime"
    type_model_uri = VACOREIM.DateTime


class Identifier(string):
    """ A string value that uniquely identifies a specific instance of an object in a dataset or document. Identifiers should be persistent, machine-resolvable, and unique within their intended scope of use. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Identifier"
    type_model_uri = VACOREIM.Identifier


# Class references



@dataclass
class Element(YAMLRoot):
    """
    The base definition for all elements that comprise the model (core, domain entity, and utility classes, value sets)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Element
    class_class_curie: ClassVar[str] = "vacoreim:Element"
    class_name: ClassVar[str] = "Element"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Element

    type: string = None
    description: Optional[str] = None
    extensions: Optional[Union[Union[dict, "Extension"], List[Union[dict, "Extension"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, string):
            self.type = string(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="extensions", slot_type=Extension, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Entity(Element):
    """
    Anything that exists, has existed, or will exist.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Entity
    class_class_curie: ClassVar[str] = "vacoreim:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Entity

    type: string = None
    id: string = None
    identifiers: Optional[Union[string, List[string]]] = empty_list()
    label: Optional[str] = None
    urls: Optional[Union[string, List[string]]] = empty_list()
    xrefs: Optional[Union[str, List[str]]] = empty_list()
    recordMetadata: Optional[Union[dict, "RecordMetadata"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, string):
            self.id = string(self.id)

        if not isinstance(self.identifiers, list):
            self.identifiers = [self.identifiers] if self.identifiers is not None else []
        self.identifiers = [v if isinstance(v, string) else string(v) for v in self.identifiers]

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.urls, list):
            self.urls = [self.urls] if self.urls is not None else []
        self.urls = [v if isinstance(v, string) else string(v) for v in self.urls]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.recordMetadata is not None and not isinstance(self.recordMetadata, RecordMetadata):
            self.recordMetadata = RecordMetadata(**as_dict(self.recordMetadata))

        super().__post_init__(**kwargs)


@dataclass
class InformationEntity(Entity):
    """
    An abstract (non-physical) entity that is about something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.InformationEntity
    class_class_curie: ClassVar[str] = "vacoreim:InformationEntity"
    class_name: ClassVar[str] = "InformationEntity"
    class_model_uri: ClassVar[URIRef] = VACOREIM.InformationEntity

    type: string = None
    id: string = None
    contributions: Optional[Union[Union[dict, "Contribution"], List[Union[dict, "Contribution"]]]] = empty_list()
    dateAuthored: Optional[string] = None
    specifiedBy: Optional[Union[Union[dict, "Method"], List[Union[dict, "Method"]]]] = empty_list()
    derivedFrom: Optional[Union[Union[dict, "InformationEntity"], List[Union[dict, "InformationEntity"]]]] = empty_list()
    reportedIn: Optional[Union[Union[dict, "Document"], List[Union[dict, "Document"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="contributions", slot_type=Contribution, key_name="type", keyed=False)

        if self.dateAuthored is not None and not isinstance(self.dateAuthored, string):
            self.dateAuthored = string(self.dateAuthored)

        self._normalize_inlined_as_dict(slot_name="specifiedBy", slot_type=Method, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="derivedFrom", slot_type=InformationEntity, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="reportedIn", slot_type=Document, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DataItem(InformationEntity):
    """
    An InformationEntity representing an individual piece of data, generated/acquired through methods which reliably
    produce truthful information about something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.DataItem
    class_class_curie: ClassVar[str] = "vacoreim:DataItem"
    class_name: ClassVar[str] = "DataItem"
    class_model_uri: ClassVar[URIRef] = VACOREIM.DataItem

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    value: Optional[str] = None
    unit: Optional[Union[dict, "Coding"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, Coding):
            self.unit = Coding(**as_dict(self.unit))

        super().__post_init__(**kwargs)


@dataclass
class DataSet(InformationEntity):
    """
    A collection of related data items or records that are organized together in a common format or structure, to
    enable their computational manipulation as a unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.DataSet
    class_class_curie: ClassVar[str] = "vacoreim:DataSet"
    class_name: ClassVar[str] = "DataSet"
    class_model_uri: ClassVar[URIRef] = VACOREIM.DataSet

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    releaseDate: Optional[string] = None
    license: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.releaseDate is not None and not isinstance(self.releaseDate, string):
            self.releaseDate = string(self.releaseDate)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class Document(InformationEntity):
    """
    A collection of information, usually in human-readable form, intended to be read and understood together as a
    whole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Document
    class_class_curie: ClassVar[str] = "vacoreim:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Document

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    title: Optional[str] = None
    license: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class Statement(InformationEntity):
    """
    An information entity expressing a declarative sentence that is either true or false.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Statement
    class_class_curie: ClassVar[str] = "vacoreim:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Statement

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    statementText: Optional[str] = None
    confidenceDirection: Optional[Union[dict, "Coding"]] = None
    confidenceLevel: Optional[Union[dict, "Coding"]] = None
    confidenceScore: Optional[Union[dict, DataItem]] = None
    evidenceDirection: Optional[str] = None
    evidenceLevel: Optional[Union[dict, "Coding"]] = None
    evidenceScore: Optional[Union[dict, DataItem]] = None
    conclusion: Optional[Union[dict, "Coding"]] = None
    hasEvidence: Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]] = empty_list()
    hasEvidenceLines: Optional[Union[Union[dict, "EvidenceLine"], List[Union[dict, "EvidenceLine"]]]] = empty_list()
    hasEvidenceOfTypes: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.statementText is not None and not isinstance(self.statementText, str):
            self.statementText = str(self.statementText)

        if self.confidenceDirection is not None and not isinstance(self.confidenceDirection, Coding):
            self.confidenceDirection = Coding(**as_dict(self.confidenceDirection))

        if self.confidenceLevel is not None and not isinstance(self.confidenceLevel, Coding):
            self.confidenceLevel = Coding(**as_dict(self.confidenceLevel))

        if self.confidenceScore is not None and not isinstance(self.confidenceScore, DataItem):
            self.confidenceScore = DataItem(**as_dict(self.confidenceScore))

        if self.evidenceDirection is not None and not isinstance(self.evidenceDirection, str):
            self.evidenceDirection = str(self.evidenceDirection)

        if self.evidenceLevel is not None and not isinstance(self.evidenceLevel, Coding):
            self.evidenceLevel = Coding(**as_dict(self.evidenceLevel))

        if self.evidenceScore is not None and not isinstance(self.evidenceScore, DataItem):
            self.evidenceScore = DataItem(**as_dict(self.evidenceScore))

        if self.conclusion is not None and not isinstance(self.conclusion, Coding):
            self.conclusion = Coding(**as_dict(self.conclusion))

        self._normalize_inlined_as_dict(slot_name="hasEvidence", slot_type=InformationEntity, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="hasEvidenceLines", slot_type=EvidenceLine, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="hasEvidenceOfTypes", slot_type=Coding, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class StudyResult(InformationEntity):
    """
    A collection of data items from a single study that are about a particular subject or experimental unit in the
    study (along with optional provenance metadata describing how these data items were generated).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.StudyResult
    class_class_curie: ClassVar[str] = "vacoreim:StudyResult"
    class_name: ClassVar[str] = "StudyResult"
    class_model_uri: ClassVar[URIRef] = VACOREIM.StudyResult

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    focus: Optional[Union[dict, Entity]] = None
    dataItems: Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]] = empty_list()
    derivedFrom: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity(**as_dict(self.focus))

        self._normalize_inlined_as_dict(slot_name="dataItems", slot_type=DataItem, key_name="type", keyed=False)

        if self.derivedFrom is not None and not isinstance(self.derivedFrom, str):
            self.derivedFrom = str(self.derivedFrom)

        if self.derivedFrom is not None and not isinstance(self.derivedFrom, DataSet):
            self.derivedFrom = DataSet(**as_dict(self.derivedFrom))

        super().__post_init__(**kwargs)


@dataclass
class EvidenceLine(InformationEntity):
    """
    A discrete, independent argument relevant to the validity of the Proposition put forth as true in the Statement,
    that is based on the interpretation of one or more pieces of information as evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.EvidenceLine
    class_class_curie: ClassVar[str] = "vacoreim:EvidenceLine"
    class_name: ClassVar[str] = "EvidenceLine"
    class_model_uri: ClassVar[URIRef] = VACOREIM.EvidenceLine

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    targetProposition: Optional[Union[dict, "Proposition"]] = None
    evidenceItems: Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]] = empty_list()
    directionOfEvidenceProvided: Optional[Union[dict, "Coding"]] = None
    strengthOfEvidenceProvided: Optional[Union[dict, "Coding"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.targetProposition is not None and not isinstance(self.targetProposition, Proposition):
            self.targetProposition = Proposition(**as_dict(self.targetProposition))

        self._normalize_inlined_as_dict(slot_name="evidenceItems", slot_type=InformationEntity, key_name="type", keyed=False)

        if self.directionOfEvidenceProvided is not None and not isinstance(self.directionOfEvidenceProvided, Coding):
            self.directionOfEvidenceProvided = Coding(**as_dict(self.directionOfEvidenceProvided))

        if self.strengthOfEvidenceProvided is not None and not isinstance(self.strengthOfEvidenceProvided, Coding):
            self.strengthOfEvidenceProvided = Coding(**as_dict(self.strengthOfEvidenceProvided))

        super().__post_init__(**kwargs)


@dataclass
class Method(InformationEntity):
    """
    A set of instructions that specify how to achieve some objective (e.g. study/experimental protocols, curation
    guidelines, rule sets, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Method
    class_class_curie: ClassVar[str] = "vacoreim:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Method

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    license: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        super().__post_init__(**kwargs)


@dataclass
class Activity(Entity):
    """
    An action or set of actions performed by an agent, that occurs over a period of time. Activities may use,
    generate, modify, move, or destroy one or more entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Activity
    class_class_curie: ClassVar[str] = "vacoreim:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Activity

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    date: Optional[string] = None
    performedBy: Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]] = empty_list()
    input: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    output: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    specifiedBy: Optional[Union[Union[dict, Method], List[Union[dict, Method]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.date is not None and not isinstance(self.date, string):
            self.date = string(self.date)

        self._normalize_inlined_as_dict(slot_name="performedBy", slot_type=Agent, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="input", slot_type=Entity, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="output", slot_type=Entity, key_name="type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="specifiedBy", slot_type=Method, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Contribution(Activity):
    """
    The actions taken by a particular agent in the creation, modification, assessment, or deprecation of some entity
    (e.g. a Statement, Evidence Line, Data Item, Publication, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Contribution
    class_class_curie: ClassVar[str] = "vacoreim:Contribution"
    class_name: ClassVar[str] = "Contribution"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Contribution

    type: string = None
    id: string = None
    contributionMadeTo: Optional[Union[dict, InformationEntity]] = None
    activity: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contributionMadeTo is not None and not isinstance(self.contributionMadeTo, InformationEntity):
            self.contributionMadeTo = InformationEntity(**as_dict(self.contributionMadeTo))

        self._normalize_inlined_as_dict(slot_name="activity", slot_type=Coding, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Agent(Entity):
    """
    An autonomous actor (person, organization, or computational agent) that bears some form of responsibility for an
    activity taking place, for the existence of an entity, or for another agent’s activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Agent
    class_class_curie: ClassVar[str] = "vacoreim:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Agent

    type: string = None
    id: string = None
    subtype: Optional[Union[dict, "Coding"]] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Proposition(Entity):
    """
    An abstract entity representing the sharable meaning that can be put forth as true or false in a Statement made by
    an Agent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Proposition
    class_class_curie: ClassVar[str] = "vacoreim:Proposition"
    class_name: ClassVar[str] = "Proposition"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Proposition

    type: string = None
    id: string = None
    subject: Union[dict, Element] = None
    predicate: Union[dict, "Coding"] = None
    object: Union[dict, Element] = None
    subtype: Optional[Union[dict, "Coding"]] = None
    propositionText: Optional[str] = None
    qualifiers: Optional[Union[Union[dict, Element], List[Union[dict, Element]]]] = empty_list()
    negated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, Element):
            self.subject = Element(**as_dict(self.subject))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, Coding):
            self.predicate = Coding(**as_dict(self.predicate))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Element):
            self.object = Element(**as_dict(self.object))

        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.propositionText is not None and not isinstance(self.propositionText, str):
            self.propositionText = str(self.propositionText)

        self._normalize_inlined_as_dict(slot_name="qualifiers", slot_type=Element, key_name="type", keyed=False)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        super().__post_init__(**kwargs)


@dataclass
class Utility(Element):
    """
    An abstract organizational class that groups complex datatype-like classes - which provide re-usable collections
    of fields that can be plugged into other objects to capture related information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Utility
    class_class_curie: ClassVar[str] = "vacoreim:Utility"
    class_name: ClassVar[str] = "Utility"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Utility

    type: string = None

@dataclass
class Coding(Utility):
    """
    A structured representation of a coded/enumerated data value, that may include additional metadata about the code
    and code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Coding
    class_class_curie: ClassVar[str] = "vacoreim:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Coding

    type: string = None
    code: Optional[string] = None
    label: Optional[str] = None
    system: Optional[str] = None
    systemURL: Optional[string] = None
    systemVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.code is not None and not isinstance(self.code, string):
            self.code = string(self.code)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.system is not None and not isinstance(self.system, str):
            self.system = str(self.system)

        if self.systemURL is not None and not isinstance(self.systemURL, string):
            self.systemURL = string(self.systemURL)

        if self.systemVersion is not None and not isinstance(self.systemVersion, str):
            self.systemVersion = str(self.systemVersion)

        super().__post_init__(**kwargs)


@dataclass
class Expression(Utility):
    """
    A structure for labels representing systematic expressions that describe an entity, as generated by formal
    nomenclatures (e.g. HGVS for genetic variants, ISCN for karyotypes, HLA nomenclature for HLA genes/alleles).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Expression
    class_class_curie: ClassVar[str] = "vacoreim:Expression"
    class_name: ClassVar[str] = "Expression"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Expression

    type: string = None
    value: str = None
    system: str = None
    systemURL: Optional[string] = None
    systemVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.systemURL is not None and not isinstance(self.systemURL, string):
            self.systemURL = string(self.systemURL)

        if self.systemVersion is not None and not isinstance(self.systemVersion, str):
            self.systemVersion = str(self.systemVersion)

        super().__post_init__(**kwargs)


@dataclass
class Extension(Utility):
    """
    A data structure that allows implementations to define and create custom fields within an Entity to capture
    information not supported by the core specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.Extension
    class_class_curie: ClassVar[str] = "vacoreim:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = VACOREIM.Extension

    type: string = None
    value: Union[dict, Element] = None
    description: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Element):
            self.value = Element(**as_dict(self.value))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class RecordMetadata(Utility):
    """
    A data structure that encapsulates provenance metadata that applies to a specific concrete record/encoding of
    information, as opposed to provenance of the abstract information content/knowledge the record represents.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VACOREIM.RecordMetadata
    class_class_curie: ClassVar[str] = "vacoreim:RecordMetadata"
    class_name: ClassVar[str] = "RecordMetadata"
    class_model_uri: ClassVar[URIRef] = VACOREIM.RecordMetadata

    type: string = None
    recordIdentifier: Optional[string] = None
    recordVersion: Optional[str] = None
    derivedFrom: Optional[Union[string, List[string]]] = empty_list()
    dateRecordCreated: Optional[string] = None
    contributions: Optional[Union[Union[dict, Contribution], List[Union[dict, Contribution]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.recordIdentifier is not None and not isinstance(self.recordIdentifier, string):
            self.recordIdentifier = string(self.recordIdentifier)

        if self.recordVersion is not None and not isinstance(self.recordVersion, str):
            self.recordVersion = str(self.recordVersion)

        if not isinstance(self.derivedFrom, list):
            self.derivedFrom = [self.derivedFrom] if self.derivedFrom is not None else []
        self.derivedFrom = [v if isinstance(v, string) else string(v) for v in self.derivedFrom]

        if self.dateRecordCreated is not None and not isinstance(self.dateRecordCreated, string):
            self.dateRecordCreated = string(self.dateRecordCreated)

        self._normalize_inlined_as_dict(slot_name="contributions", slot_type=Contribution, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.type = Slot(uri=VACOREIM.type, name="type", curie=VACOREIM.curie('type'),
                   model_uri=VACOREIM.type, domain=None, range=Optional[str])

slots.description = Slot(uri=VACOREIM.description, name="description", curie=VACOREIM.curie('description'),
                   model_uri=VACOREIM.description, domain=None, range=Optional[str])

slots.extensions = Slot(uri=VACOREIM.extensions, name="extensions", curie=VACOREIM.curie('extensions'),
                   model_uri=VACOREIM.extensions, domain=None, range=Optional[str])

slots.id = Slot(uri=VACOREIM.id, name="id", curie=VACOREIM.curie('id'),
                   model_uri=VACOREIM.id, domain=None, range=Optional[str])

slots.identifiers = Slot(uri=VACOREIM.identifiers, name="identifiers", curie=VACOREIM.curie('identifiers'),
                   model_uri=VACOREIM.identifiers, domain=None, range=Optional[str])

slots.label = Slot(uri=VACOREIM.label, name="label", curie=VACOREIM.curie('label'),
                   model_uri=VACOREIM.label, domain=None, range=Optional[str])

slots.urls = Slot(uri=VACOREIM.urls, name="urls", curie=VACOREIM.curie('urls'),
                   model_uri=VACOREIM.urls, domain=None, range=Optional[str])

slots.xrefs = Slot(uri=VACOREIM.xrefs, name="xrefs", curie=VACOREIM.curie('xrefs'),
                   model_uri=VACOREIM.xrefs, domain=None, range=Optional[str])

slots.recordMetadata = Slot(uri=VACOREIM.recordMetadata, name="recordMetadata", curie=VACOREIM.curie('recordMetadata'),
                   model_uri=VACOREIM.recordMetadata, domain=None, range=Optional[str])

slots.contributions = Slot(uri=VACOREIM.contributions, name="contributions", curie=VACOREIM.curie('contributions'),
                   model_uri=VACOREIM.contributions, domain=None, range=Optional[str])

slots.dateAuthored = Slot(uri=VACOREIM.dateAuthored, name="dateAuthored", curie=VACOREIM.curie('dateAuthored'),
                   model_uri=VACOREIM.dateAuthored, domain=None, range=Optional[str])

slots.specifiedBy = Slot(uri=VACOREIM.specifiedBy, name="specifiedBy", curie=VACOREIM.curie('specifiedBy'),
                   model_uri=VACOREIM.specifiedBy, domain=None, range=Optional[str])

slots.derivedFrom = Slot(uri=VACOREIM.derivedFrom, name="derivedFrom", curie=VACOREIM.curie('derivedFrom'),
                   model_uri=VACOREIM.derivedFrom, domain=None, range=Optional[str])

slots.reportedIn = Slot(uri=VACOREIM.reportedIn, name="reportedIn", curie=VACOREIM.curie('reportedIn'),
                   model_uri=VACOREIM.reportedIn, domain=None, range=Optional[str])

slots.subtype = Slot(uri=VACOREIM.subtype, name="subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.subtype, domain=None, range=Optional[str])

slots.value = Slot(uri=VACOREIM.value, name="value", curie=VACOREIM.curie('value'),
                   model_uri=VACOREIM.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=VACOREIM.unit, name="unit", curie=VACOREIM.curie('unit'),
                   model_uri=VACOREIM.unit, domain=None, range=Optional[str])

slots.releaseDate = Slot(uri=VACOREIM.releaseDate, name="releaseDate", curie=VACOREIM.curie('releaseDate'),
                   model_uri=VACOREIM.releaseDate, domain=None, range=Optional[str])

slots.license = Slot(uri=VACOREIM.license, name="license", curie=VACOREIM.curie('license'),
                   model_uri=VACOREIM.license, domain=None, range=Optional[str])

slots.version = Slot(uri=VACOREIM.version, name="version", curie=VACOREIM.curie('version'),
                   model_uri=VACOREIM.version, domain=None, range=Optional[str])

slots.title = Slot(uri=VACOREIM.title, name="title", curie=VACOREIM.curie('title'),
                   model_uri=VACOREIM.title, domain=None, range=Optional[str])

slots.statementText = Slot(uri=VACOREIM.statementText, name="statementText", curie=VACOREIM.curie('statementText'),
                   model_uri=VACOREIM.statementText, domain=None, range=Optional[str])

slots.confidenceDirection = Slot(uri=VACOREIM.confidenceDirection, name="confidenceDirection", curie=VACOREIM.curie('confidenceDirection'),
                   model_uri=VACOREIM.confidenceDirection, domain=None, range=Optional[str])

slots.confidenceLevel = Slot(uri=VACOREIM.confidenceLevel, name="confidenceLevel", curie=VACOREIM.curie('confidenceLevel'),
                   model_uri=VACOREIM.confidenceLevel, domain=None, range=Optional[str])

slots.confidenceScore = Slot(uri=VACOREIM.confidenceScore, name="confidenceScore", curie=VACOREIM.curie('confidenceScore'),
                   model_uri=VACOREIM.confidenceScore, domain=None, range=Optional[str])

slots.evidenceDirection = Slot(uri=VACOREIM.evidenceDirection, name="evidenceDirection", curie=VACOREIM.curie('evidenceDirection'),
                   model_uri=VACOREIM.evidenceDirection, domain=None, range=Optional[str])

slots.evidenceLevel = Slot(uri=VACOREIM.evidenceLevel, name="evidenceLevel", curie=VACOREIM.curie('evidenceLevel'),
                   model_uri=VACOREIM.evidenceLevel, domain=None, range=Optional[str])

slots.evidenceScore = Slot(uri=VACOREIM.evidenceScore, name="evidenceScore", curie=VACOREIM.curie('evidenceScore'),
                   model_uri=VACOREIM.evidenceScore, domain=None, range=Optional[str])

slots.conclusion = Slot(uri=VACOREIM.conclusion, name="conclusion", curie=VACOREIM.curie('conclusion'),
                   model_uri=VACOREIM.conclusion, domain=None, range=Optional[str])

slots.hasEvidence = Slot(uri=VACOREIM.hasEvidence, name="hasEvidence", curie=VACOREIM.curie('hasEvidence'),
                   model_uri=VACOREIM.hasEvidence, domain=None, range=Optional[str])

slots.hasEvidenceLines = Slot(uri=VACOREIM.hasEvidenceLines, name="hasEvidenceLines", curie=VACOREIM.curie('hasEvidenceLines'),
                   model_uri=VACOREIM.hasEvidenceLines, domain=None, range=Optional[str])

slots.hasEvidenceOfTypes = Slot(uri=VACOREIM.hasEvidenceOfTypes, name="hasEvidenceOfTypes", curie=VACOREIM.curie('hasEvidenceOfTypes'),
                   model_uri=VACOREIM.hasEvidenceOfTypes, domain=None, range=Optional[str])

slots.focus = Slot(uri=VACOREIM.focus, name="focus", curie=VACOREIM.curie('focus'),
                   model_uri=VACOREIM.focus, domain=None, range=Optional[str])

slots.dataItems = Slot(uri=VACOREIM.dataItems, name="dataItems", curie=VACOREIM.curie('dataItems'),
                   model_uri=VACOREIM.dataItems, domain=None, range=Optional[str])

slots.targetProposition = Slot(uri=VACOREIM.targetProposition, name="targetProposition", curie=VACOREIM.curie('targetProposition'),
                   model_uri=VACOREIM.targetProposition, domain=None, range=Optional[str])

slots.evidenceItems = Slot(uri=VACOREIM.evidenceItems, name="evidenceItems", curie=VACOREIM.curie('evidenceItems'),
                   model_uri=VACOREIM.evidenceItems, domain=None, range=Optional[str])

slots.directionOfEvidenceProvided = Slot(uri=VACOREIM.directionOfEvidenceProvided, name="directionOfEvidenceProvided", curie=VACOREIM.curie('directionOfEvidenceProvided'),
                   model_uri=VACOREIM.directionOfEvidenceProvided, domain=None, range=Optional[str])

slots.strengthOfEvidenceProvided = Slot(uri=VACOREIM.strengthOfEvidenceProvided, name="strengthOfEvidenceProvided", curie=VACOREIM.curie('strengthOfEvidenceProvided'),
                   model_uri=VACOREIM.strengthOfEvidenceProvided, domain=None, range=Optional[str])

slots.date = Slot(uri=VACOREIM.date, name="date", curie=VACOREIM.curie('date'),
                   model_uri=VACOREIM.date, domain=None, range=Optional[str])

slots.performedBy = Slot(uri=VACOREIM.performedBy, name="performedBy", curie=VACOREIM.curie('performedBy'),
                   model_uri=VACOREIM.performedBy, domain=None, range=Optional[str])

slots.input = Slot(uri=VACOREIM.input, name="input", curie=VACOREIM.curie('input'),
                   model_uri=VACOREIM.input, domain=None, range=Optional[str])

slots.output = Slot(uri=VACOREIM.output, name="output", curie=VACOREIM.curie('output'),
                   model_uri=VACOREIM.output, domain=None, range=Optional[str])

slots.contributionMadeTo = Slot(uri=VACOREIM.contributionMadeTo, name="contributionMadeTo", curie=VACOREIM.curie('contributionMadeTo'),
                   model_uri=VACOREIM.contributionMadeTo, domain=None, range=Optional[str])

slots.activity = Slot(uri=VACOREIM.activity, name="activity", curie=VACOREIM.curie('activity'),
                   model_uri=VACOREIM.activity, domain=None, range=Optional[str])

slots.name = Slot(uri=VACOREIM.name, name="name", curie=VACOREIM.curie('name'),
                   model_uri=VACOREIM.name, domain=None, range=Optional[str])

slots.propositionText = Slot(uri=VACOREIM.propositionText, name="propositionText", curie=VACOREIM.curie('propositionText'),
                   model_uri=VACOREIM.propositionText, domain=None, range=Optional[str])

slots.subject = Slot(uri=VACOREIM.subject, name="subject", curie=VACOREIM.curie('subject'),
                   model_uri=VACOREIM.subject, domain=None, range=Optional[str])

slots.predicate = Slot(uri=VACOREIM.predicate, name="predicate", curie=VACOREIM.curie('predicate'),
                   model_uri=VACOREIM.predicate, domain=None, range=Optional[str])

slots.object = Slot(uri=VACOREIM.object, name="object", curie=VACOREIM.curie('object'),
                   model_uri=VACOREIM.object, domain=None, range=Optional[str])

slots.qualifiers = Slot(uri=VACOREIM.qualifiers, name="qualifiers", curie=VACOREIM.curie('qualifiers'),
                   model_uri=VACOREIM.qualifiers, domain=None, range=Optional[str])

slots.negated = Slot(uri=VACOREIM.negated, name="negated", curie=VACOREIM.curie('negated'),
                   model_uri=VACOREIM.negated, domain=None, range=Optional[str])

slots.code = Slot(uri=VACOREIM.code, name="code", curie=VACOREIM.curie('code'),
                   model_uri=VACOREIM.code, domain=None, range=Optional[str])

slots.system = Slot(uri=VACOREIM.system, name="system", curie=VACOREIM.curie('system'),
                   model_uri=VACOREIM.system, domain=None, range=Optional[str])

slots.systemURL = Slot(uri=VACOREIM.systemURL, name="systemURL", curie=VACOREIM.curie('systemURL'),
                   model_uri=VACOREIM.systemURL, domain=None, range=Optional[str])

slots.systemVersion = Slot(uri=VACOREIM.systemVersion, name="systemVersion", curie=VACOREIM.curie('systemVersion'),
                   model_uri=VACOREIM.systemVersion, domain=None, range=Optional[str])

slots.recordIdentifier = Slot(uri=VACOREIM.recordIdentifier, name="recordIdentifier", curie=VACOREIM.curie('recordIdentifier'),
                   model_uri=VACOREIM.recordIdentifier, domain=None, range=Optional[str])

slots.recordVersion = Slot(uri=VACOREIM.recordVersion, name="recordVersion", curie=VACOREIM.curie('recordVersion'),
                   model_uri=VACOREIM.recordVersion, domain=None, range=Optional[str])

slots.dateRecordCreated = Slot(uri=VACOREIM.dateRecordCreated, name="dateRecordCreated", curie=VACOREIM.curie('dateRecordCreated'),
                   model_uri=VACOREIM.dateRecordCreated, domain=None, range=Optional[str])

slots.Element_type = Slot(uri=VACOREIM.type, name="Element_type", curie=VACOREIM.curie('type'),
                   model_uri=VACOREIM.Element_type, domain=Element, range=string)

slots.Element_description = Slot(uri=VACOREIM.description, name="Element_description", curie=VACOREIM.curie('description'),
                   model_uri=VACOREIM.Element_description, domain=Element, range=Optional[str])

slots.Element_extensions = Slot(uri=VACOREIM.extensions, name="Element_extensions", curie=VACOREIM.curie('extensions'),
                   model_uri=VACOREIM.Element_extensions, domain=Element, range=Optional[Union[Union[dict, "Extension"], List[Union[dict, "Extension"]]]])

slots.Entity_id = Slot(uri=VACOREIM.id, name="Entity_id", curie=VACOREIM.curie('id'),
                   model_uri=VACOREIM.Entity_id, domain=Entity, range=string)

slots.Entity_identifiers = Slot(uri=VACOREIM.identifiers, name="Entity_identifiers", curie=VACOREIM.curie('identifiers'),
                   model_uri=VACOREIM.Entity_identifiers, domain=Entity, range=Optional[Union[string, List[string]]])

slots.Entity_label = Slot(uri=VACOREIM.label, name="Entity_label", curie=VACOREIM.curie('label'),
                   model_uri=VACOREIM.Entity_label, domain=Entity, range=Optional[str])

slots.Entity_urls = Slot(uri=VACOREIM.urls, name="Entity_urls", curie=VACOREIM.curie('urls'),
                   model_uri=VACOREIM.Entity_urls, domain=Entity, range=Optional[Union[string, List[string]]])

slots.Entity_xrefs = Slot(uri=VACOREIM.xrefs, name="Entity_xrefs", curie=VACOREIM.curie('xrefs'),
                   model_uri=VACOREIM.Entity_xrefs, domain=Entity, range=Optional[Union[str, List[str]]])

slots.Entity_recordMetadata = Slot(uri=VACOREIM.recordMetadata, name="Entity_recordMetadata", curie=VACOREIM.curie('recordMetadata'),
                   model_uri=VACOREIM.Entity_recordMetadata, domain=Entity, range=Optional[Union[dict, "RecordMetadata"]])

slots.InformationEntity_contributions = Slot(uri=VACOREIM.contributions, name="InformationEntity_contributions", curie=VACOREIM.curie('contributions'),
                   model_uri=VACOREIM.InformationEntity_contributions, domain=InformationEntity, range=Optional[Union[Union[dict, "Contribution"], List[Union[dict, "Contribution"]]]])

slots.InformationEntity_dateAuthored = Slot(uri=VACOREIM.dateAuthored, name="InformationEntity_dateAuthored", curie=VACOREIM.curie('dateAuthored'),
                   model_uri=VACOREIM.InformationEntity_dateAuthored, domain=InformationEntity, range=Optional[string])

slots.InformationEntity_specifiedBy = Slot(uri=VACOREIM.specifiedBy, name="InformationEntity_specifiedBy", curie=VACOREIM.curie('specifiedBy'),
                   model_uri=VACOREIM.InformationEntity_specifiedBy, domain=InformationEntity, range=Optional[Union[Union[dict, "Method"], List[Union[dict, "Method"]]]])

slots.InformationEntity_derivedFrom = Slot(uri=VACOREIM.derivedFrom, name="InformationEntity_derivedFrom", curie=VACOREIM.curie('derivedFrom'),
                   model_uri=VACOREIM.InformationEntity_derivedFrom, domain=InformationEntity, range=Optional[Union[Union[dict, "InformationEntity"], List[Union[dict, "InformationEntity"]]]])

slots.InformationEntity_reportedIn = Slot(uri=VACOREIM.reportedIn, name="InformationEntity_reportedIn", curie=VACOREIM.curie('reportedIn'),
                   model_uri=VACOREIM.InformationEntity_reportedIn, domain=InformationEntity, range=Optional[Union[Union[dict, "Document"], List[Union[dict, "Document"]]]])

slots.DataItem_subtype = Slot(uri=VACOREIM.subtype, name="DataItem_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.DataItem_subtype, domain=DataItem, range=Optional[Union[dict, "Coding"]])

slots.DataItem_value = Slot(uri=VACOREIM.value, name="DataItem_value", curie=VACOREIM.curie('value'),
                   model_uri=VACOREIM.DataItem_value, domain=DataItem, range=Optional[str])

slots.DataItem_unit = Slot(uri=VACOREIM.unit, name="DataItem_unit", curie=VACOREIM.curie('unit'),
                   model_uri=VACOREIM.DataItem_unit, domain=DataItem, range=Optional[Union[dict, "Coding"]])

slots.DataSet_subtype = Slot(uri=VACOREIM.subtype, name="DataSet_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.DataSet_subtype, domain=DataSet, range=Optional[Union[dict, "Coding"]])

slots.DataSet_releaseDate = Slot(uri=VACOREIM.releaseDate, name="DataSet_releaseDate", curie=VACOREIM.curie('releaseDate'),
                   model_uri=VACOREIM.DataSet_releaseDate, domain=DataSet, range=Optional[string])

slots.DataSet_license = Slot(uri=VACOREIM.license, name="DataSet_license", curie=VACOREIM.curie('license'),
                   model_uri=VACOREIM.DataSet_license, domain=DataSet, range=Optional[str])

slots.DataSet_version = Slot(uri=VACOREIM.version, name="DataSet_version", curie=VACOREIM.curie('version'),
                   model_uri=VACOREIM.DataSet_version, domain=DataSet, range=Optional[str])

slots.Document_subtype = Slot(uri=VACOREIM.subtype, name="Document_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.Document_subtype, domain=Document, range=Optional[Union[dict, "Coding"]])

slots.Document_title = Slot(uri=VACOREIM.title, name="Document_title", curie=VACOREIM.curie('title'),
                   model_uri=VACOREIM.Document_title, domain=Document, range=Optional[str])

slots.Document_license = Slot(uri=VACOREIM.license, name="Document_license", curie=VACOREIM.curie('license'),
                   model_uri=VACOREIM.Document_license, domain=Document, range=Optional[str])

slots.Document_version = Slot(uri=VACOREIM.version, name="Document_version", curie=VACOREIM.curie('version'),
                   model_uri=VACOREIM.Document_version, domain=Document, range=Optional[str])

slots.Statement_subtype = Slot(uri=VACOREIM.subtype, name="Statement_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.Statement_subtype, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_statementText = Slot(uri=VACOREIM.statementText, name="Statement_statementText", curie=VACOREIM.curie('statementText'),
                   model_uri=VACOREIM.Statement_statementText, domain=Statement, range=Optional[str])

slots.Statement_confidenceDirection = Slot(uri=VACOREIM.confidenceDirection, name="Statement_confidenceDirection", curie=VACOREIM.curie('confidenceDirection'),
                   model_uri=VACOREIM.Statement_confidenceDirection, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_confidenceLevel = Slot(uri=VACOREIM.confidenceLevel, name="Statement_confidenceLevel", curie=VACOREIM.curie('confidenceLevel'),
                   model_uri=VACOREIM.Statement_confidenceLevel, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_confidenceScore = Slot(uri=VACOREIM.confidenceScore, name="Statement_confidenceScore", curie=VACOREIM.curie('confidenceScore'),
                   model_uri=VACOREIM.Statement_confidenceScore, domain=Statement, range=Optional[Union[dict, DataItem]])

slots.Statement_evidenceDirection = Slot(uri=VACOREIM.evidenceDirection, name="Statement_evidenceDirection", curie=VACOREIM.curie('evidenceDirection'),
                   model_uri=VACOREIM.Statement_evidenceDirection, domain=Statement, range=Optional[str])

slots.Statement_evidenceLevel = Slot(uri=VACOREIM.evidenceLevel, name="Statement_evidenceLevel", curie=VACOREIM.curie('evidenceLevel'),
                   model_uri=VACOREIM.Statement_evidenceLevel, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_evidenceScore = Slot(uri=VACOREIM.evidenceScore, name="Statement_evidenceScore", curie=VACOREIM.curie('evidenceScore'),
                   model_uri=VACOREIM.Statement_evidenceScore, domain=Statement, range=Optional[Union[dict, DataItem]])

slots.Statement_conclusion = Slot(uri=VACOREIM.conclusion, name="Statement_conclusion", curie=VACOREIM.curie('conclusion'),
                   model_uri=VACOREIM.Statement_conclusion, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_hasEvidence = Slot(uri=VACOREIM.hasEvidence, name="Statement_hasEvidence", curie=VACOREIM.curie('hasEvidence'),
                   model_uri=VACOREIM.Statement_hasEvidence, domain=Statement, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.Statement_hasEvidenceLines = Slot(uri=VACOREIM.hasEvidenceLines, name="Statement_hasEvidenceLines", curie=VACOREIM.curie('hasEvidenceLines'),
                   model_uri=VACOREIM.Statement_hasEvidenceLines, domain=Statement, range=Optional[Union[Union[dict, "EvidenceLine"], List[Union[dict, "EvidenceLine"]]]])

slots.Statement_hasEvidenceOfTypes = Slot(uri=VACOREIM.hasEvidenceOfTypes, name="Statement_hasEvidenceOfTypes", curie=VACOREIM.curie('hasEvidenceOfTypes'),
                   model_uri=VACOREIM.Statement_hasEvidenceOfTypes, domain=Statement, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.StudyResult_subtype = Slot(uri=VACOREIM.subtype, name="StudyResult_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.StudyResult_subtype, domain=StudyResult, range=Optional[Union[dict, "Coding"]])

slots.StudyResult_focus = Slot(uri=VACOREIM.focus, name="StudyResult_focus", curie=VACOREIM.curie('focus'),
                   model_uri=VACOREIM.StudyResult_focus, domain=StudyResult, range=Optional[Union[dict, Entity]])

slots.StudyResult_dataItems = Slot(uri=VACOREIM.dataItems, name="StudyResult_dataItems", curie=VACOREIM.curie('dataItems'),
                   model_uri=VACOREIM.StudyResult_dataItems, domain=StudyResult, range=Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]])

slots.StudyResult_derivedFrom = Slot(uri=VACOREIM.derivedFrom, name="StudyResult_derivedFrom", curie=VACOREIM.curie('derivedFrom'),
                   model_uri=VACOREIM.StudyResult_derivedFrom, domain=StudyResult, range=Optional[Union[dict, DataSet]])

slots.EvidenceLine_subtype = Slot(uri=VACOREIM.subtype, name="EvidenceLine_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.EvidenceLine_subtype, domain=EvidenceLine, range=Optional[Union[dict, "Coding"]])

slots.EvidenceLine_targetProposition = Slot(uri=VACOREIM.targetProposition, name="EvidenceLine_targetProposition", curie=VACOREIM.curie('targetProposition'),
                   model_uri=VACOREIM.EvidenceLine_targetProposition, domain=EvidenceLine, range=Optional[Union[dict, "Proposition"]])

slots.EvidenceLine_evidenceItems = Slot(uri=VACOREIM.evidenceItems, name="EvidenceLine_evidenceItems", curie=VACOREIM.curie('evidenceItems'),
                   model_uri=VACOREIM.EvidenceLine_evidenceItems, domain=EvidenceLine, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.EvidenceLine_directionOfEvidenceProvided = Slot(uri=VACOREIM.directionOfEvidenceProvided, name="EvidenceLine_directionOfEvidenceProvided", curie=VACOREIM.curie('directionOfEvidenceProvided'),
                   model_uri=VACOREIM.EvidenceLine_directionOfEvidenceProvided, domain=EvidenceLine, range=Optional[Union[dict, "Coding"]])

slots.EvidenceLine_strengthOfEvidenceProvided = Slot(uri=VACOREIM.strengthOfEvidenceProvided, name="EvidenceLine_strengthOfEvidenceProvided", curie=VACOREIM.curie('strengthOfEvidenceProvided'),
                   model_uri=VACOREIM.EvidenceLine_strengthOfEvidenceProvided, domain=EvidenceLine, range=Optional[Union[dict, "Coding"]])

slots.Method_subtype = Slot(uri=VACOREIM.subtype, name="Method_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.Method_subtype, domain=Method, range=Optional[Union[dict, "Coding"]])

slots.Method_license = Slot(uri=VACOREIM.license, name="Method_license", curie=VACOREIM.curie('license'),
                   model_uri=VACOREIM.Method_license, domain=Method, range=Optional[str])

slots.Activity_subtype = Slot(uri=VACOREIM.subtype, name="Activity_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.Activity_subtype, domain=Activity, range=Optional[Union[dict, "Coding"]])

slots.Activity_date = Slot(uri=VACOREIM.date, name="Activity_date", curie=VACOREIM.curie('date'),
                   model_uri=VACOREIM.Activity_date, domain=Activity, range=Optional[string])

slots.Activity_performedBy = Slot(uri=VACOREIM.performedBy, name="Activity_performedBy", curie=VACOREIM.curie('performedBy'),
                   model_uri=VACOREIM.Activity_performedBy, domain=Activity, range=Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]])

slots.Activity_input = Slot(uri=VACOREIM.input, name="Activity_input", curie=VACOREIM.curie('input'),
                   model_uri=VACOREIM.Activity_input, domain=Activity, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.Activity_output = Slot(uri=VACOREIM.output, name="Activity_output", curie=VACOREIM.curie('output'),
                   model_uri=VACOREIM.Activity_output, domain=Activity, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.Activity_specifiedBy = Slot(uri=VACOREIM.specifiedBy, name="Activity_specifiedBy", curie=VACOREIM.curie('specifiedBy'),
                   model_uri=VACOREIM.Activity_specifiedBy, domain=Activity, range=Optional[Union[Union[dict, Method], List[Union[dict, Method]]]])

slots.Contribution_contributionMadeTo = Slot(uri=VACOREIM.contributionMadeTo, name="Contribution_contributionMadeTo", curie=VACOREIM.curie('contributionMadeTo'),
                   model_uri=VACOREIM.Contribution_contributionMadeTo, domain=Contribution, range=Optional[Union[dict, InformationEntity]])

slots.Contribution_activity = Slot(uri=VACOREIM.activity, name="Contribution_activity", curie=VACOREIM.curie('activity'),
                   model_uri=VACOREIM.Contribution_activity, domain=Contribution, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Agent_subtype = Slot(uri=VACOREIM.subtype, name="Agent_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.Agent_subtype, domain=Agent, range=Optional[Union[dict, "Coding"]])

slots.Proposition_subtype = Slot(uri=VACOREIM.subtype, name="Proposition_subtype", curie=VACOREIM.curie('subtype'),
                   model_uri=VACOREIM.Proposition_subtype, domain=Proposition, range=Optional[Union[dict, "Coding"]])

slots.Proposition_propositionText = Slot(uri=VACOREIM.propositionText, name="Proposition_propositionText", curie=VACOREIM.curie('propositionText'),
                   model_uri=VACOREIM.Proposition_propositionText, domain=Proposition, range=Optional[str])

slots.Proposition_subject = Slot(uri=VACOREIM.subject, name="Proposition_subject", curie=VACOREIM.curie('subject'),
                   model_uri=VACOREIM.Proposition_subject, domain=Proposition, range=Union[dict, Element])

slots.Proposition_predicate = Slot(uri=VACOREIM.predicate, name="Proposition_predicate", curie=VACOREIM.curie('predicate'),
                   model_uri=VACOREIM.Proposition_predicate, domain=Proposition, range=Union[dict, "Coding"])

slots.Proposition_object = Slot(uri=VACOREIM.object, name="Proposition_object", curie=VACOREIM.curie('object'),
                   model_uri=VACOREIM.Proposition_object, domain=Proposition, range=Union[dict, Element])

slots.Proposition_qualifiers = Slot(uri=VACOREIM.qualifiers, name="Proposition_qualifiers", curie=VACOREIM.curie('qualifiers'),
                   model_uri=VACOREIM.Proposition_qualifiers, domain=Proposition, range=Optional[Union[Union[dict, Element], List[Union[dict, Element]]]])

slots.Proposition_negated = Slot(uri=VACOREIM.negated, name="Proposition_negated", curie=VACOREIM.curie('negated'),
                   model_uri=VACOREIM.Proposition_negated, domain=Proposition, range=Optional[Union[bool, Bool]])

slots.Coding_code = Slot(uri=VACOREIM.code, name="Coding_code", curie=VACOREIM.curie('code'),
                   model_uri=VACOREIM.Coding_code, domain=Coding, range=Optional[string])

slots.Coding_label = Slot(uri=VACOREIM.label, name="Coding_label", curie=VACOREIM.curie('label'),
                   model_uri=VACOREIM.Coding_label, domain=Coding, range=Optional[str])

slots.Coding_system = Slot(uri=VACOREIM.system, name="Coding_system", curie=VACOREIM.curie('system'),
                   model_uri=VACOREIM.Coding_system, domain=Coding, range=Optional[str])

slots.Coding_systemURL = Slot(uri=VACOREIM.systemURL, name="Coding_systemURL", curie=VACOREIM.curie('systemURL'),
                   model_uri=VACOREIM.Coding_systemURL, domain=Coding, range=Optional[string])

slots.Coding_systemVersion = Slot(uri=VACOREIM.systemVersion, name="Coding_systemVersion", curie=VACOREIM.curie('systemVersion'),
                   model_uri=VACOREIM.Coding_systemVersion, domain=Coding, range=Optional[str])

slots.Expression_value = Slot(uri=VACOREIM.value, name="Expression_value", curie=VACOREIM.curie('value'),
                   model_uri=VACOREIM.Expression_value, domain=Expression, range=str)

slots.Expression_system = Slot(uri=VACOREIM.system, name="Expression_system", curie=VACOREIM.curie('system'),
                   model_uri=VACOREIM.Expression_system, domain=Expression, range=str)

slots.Expression_systemURL = Slot(uri=VACOREIM.systemURL, name="Expression_systemURL", curie=VACOREIM.curie('systemURL'),
                   model_uri=VACOREIM.Expression_systemURL, domain=Expression, range=Optional[string])

slots.Expression_systemVersion = Slot(uri=VACOREIM.systemVersion, name="Expression_systemVersion", curie=VACOREIM.curie('systemVersion'),
                   model_uri=VACOREIM.Expression_systemVersion, domain=Expression, range=Optional[str])

slots.Extension_description = Slot(uri=VACOREIM.description, name="Extension_description", curie=VACOREIM.curie('description'),
                   model_uri=VACOREIM.Extension_description, domain=Extension, range=Optional[str])

slots.Extension_value = Slot(uri=VACOREIM.value, name="Extension_value", curie=VACOREIM.curie('value'),
                   model_uri=VACOREIM.Extension_value, domain=Extension, range=Union[dict, Element])

slots.RecordMetadata_recordIdentifier = Slot(uri=VACOREIM.recordIdentifier, name="RecordMetadata_recordIdentifier", curie=VACOREIM.curie('recordIdentifier'),
                   model_uri=VACOREIM.RecordMetadata_recordIdentifier, domain=RecordMetadata, range=Optional[string])

slots.RecordMetadata_recordVersion = Slot(uri=VACOREIM.recordVersion, name="RecordMetadata_recordVersion", curie=VACOREIM.curie('recordVersion'),
                   model_uri=VACOREIM.RecordMetadata_recordVersion, domain=RecordMetadata, range=Optional[str])

slots.RecordMetadata_derivedFrom = Slot(uri=VACOREIM.derivedFrom, name="RecordMetadata_derivedFrom", curie=VACOREIM.curie('derivedFrom'),
                   model_uri=VACOREIM.RecordMetadata_derivedFrom, domain=RecordMetadata, range=Optional[Union[string, List[string]]])

slots.RecordMetadata_dateRecordCreated = Slot(uri=VACOREIM.dateRecordCreated, name="RecordMetadata_dateRecordCreated", curie=VACOREIM.curie('dateRecordCreated'),
                   model_uri=VACOREIM.RecordMetadata_dateRecordCreated, domain=RecordMetadata, range=Optional[string])

slots.RecordMetadata_contributions = Slot(uri=VACOREIM.contributions, name="RecordMetadata_contributions", curie=VACOREIM.curie('contributions'),
                   model_uri=VACOREIM.RecordMetadata_contributions, domain=RecordMetadata, range=Optional[Union[Union[dict, Contribution], List[Union[dict, Contribution]]]])