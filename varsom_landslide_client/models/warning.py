# coding: utf-8

"""
    Jordskredvarsel API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Warning(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'event_id': 'str',
        'id': 'str',
        'master_id': 'str',
        'version': 'int',
        'lang_key': 'int',
        'cap_status': 'str',
        'met_id': 'str',
        'met_name': 'str',
        'county_list': 'list[County]',
        'municipality_list': 'list[Municipality]',
        'municipality_csv_string': 'str',
        'activity_level': 'str',
        'activity_level_name': 'str',
        'danger_type': 'str',
        'danger_type_name': 'str',
        'valid_from': 'datetime',
        'valid_to': 'datetime',
        'next_warning_time': 'datetime',
        'publish_time': 'datetime',
        'created_time': 'datetime',
        'danger_increase_date_time': 'datetime',
        'danger_decrease_date_time': 'datetime',
        'main_text': 'str',
        'warning_text': 'str',
        'advice_text': 'str',
        'consequence_text': 'str',
        'level_meaning_text': 'str',
        'cause_text': 'str',
        'area': 'str',
        'exposed_height_type': 'int',
        'exposed_height_value': 'int',
        'exposed_height_value2': 'int',
        'exposed_climate_type': 'int',
        'cause_list': 'list[Cause]',
        'micro_blog_post_list': 'list[MicroBlogPost]',
        'station_list': 'list[Station]'
    }

    attribute_map = {
        'event_id': 'EventId',
        'id': 'Id',
        'master_id': 'MasterId',
        'version': 'Version',
        'lang_key': 'LangKey',
        'cap_status': 'CapStatus',
        'met_id': 'MetId',
        'met_name': 'MetName',
        'county_list': 'CountyList',
        'municipality_list': 'MunicipalityList',
        'municipality_csv_string': 'MunicipalityCsvString',
        'activity_level': 'ActivityLevel',
        'activity_level_name': 'ActivityLevelName',
        'danger_type': 'DangerType',
        'danger_type_name': 'DangerTypeName',
        'valid_from': 'ValidFrom',
        'valid_to': 'ValidTo',
        'next_warning_time': 'NextWarningTime',
        'publish_time': 'PublishTime',
        'created_time': 'CreatedTime',
        'danger_increase_date_time': 'DangerIncreaseDateTime',
        'danger_decrease_date_time': 'DangerDecreaseDateTime',
        'main_text': 'MainText',
        'warning_text': 'WarningText',
        'advice_text': 'AdviceText',
        'consequence_text': 'ConsequenceText',
        'level_meaning_text': 'LevelMeaningText',
        'cause_text': 'CauseText',
        'area': 'Area',
        'exposed_height_type': 'ExposedHeightType',
        'exposed_height_value': 'ExposedHeightValue',
        'exposed_height_value2': 'ExposedHeightValue2',
        'exposed_climate_type': 'ExposedClimateType',
        'cause_list': 'CauseList',
        'micro_blog_post_list': 'MicroBlogPostList',
        'station_list': 'StationList'
    }

    def __init__(self, event_id=None, id=None, master_id=None, version=None, lang_key=None, cap_status=None, met_id=None, met_name=None, county_list=None, municipality_list=None, municipality_csv_string=None, activity_level=None, activity_level_name=None, danger_type=None, danger_type_name=None, valid_from=None, valid_to=None, next_warning_time=None, publish_time=None, created_time=None, danger_increase_date_time=None, danger_decrease_date_time=None, main_text=None, warning_text=None, advice_text=None, consequence_text=None, level_meaning_text=None, cause_text=None, area=None, exposed_height_type=None, exposed_height_value=None, exposed_height_value2=None, exposed_climate_type=None, cause_list=None, micro_blog_post_list=None, station_list=None):  # noqa: E501
        """Warning - a model defined in Swagger"""  # noqa: E501
        self._event_id = None
        self._id = None
        self._master_id = None
        self._version = None
        self._lang_key = None
        self._cap_status = None
        self._met_id = None
        self._met_name = None
        self._county_list = None
        self._municipality_list = None
        self._municipality_csv_string = None
        self._activity_level = None
        self._activity_level_name = None
        self._danger_type = None
        self._danger_type_name = None
        self._valid_from = None
        self._valid_to = None
        self._next_warning_time = None
        self._publish_time = None
        self._created_time = None
        self._danger_increase_date_time = None
        self._danger_decrease_date_time = None
        self._main_text = None
        self._warning_text = None
        self._advice_text = None
        self._consequence_text = None
        self._level_meaning_text = None
        self._cause_text = None
        self._area = None
        self._exposed_height_type = None
        self._exposed_height_value = None
        self._exposed_height_value2 = None
        self._exposed_climate_type = None
        self._cause_list = None
        self._micro_blog_post_list = None
        self._station_list = None
        self.discriminator = None
        if event_id is not None:
            self.event_id = event_id
        if id is not None:
            self.id = id
        if master_id is not None:
            self.master_id = master_id
        if version is not None:
            self.version = version
        if lang_key is not None:
            self.lang_key = lang_key
        if cap_status is not None:
            self.cap_status = cap_status
        if met_id is not None:
            self.met_id = met_id
        if met_name is not None:
            self.met_name = met_name
        if county_list is not None:
            self.county_list = county_list
        if municipality_list is not None:
            self.municipality_list = municipality_list
        if municipality_csv_string is not None:
            self.municipality_csv_string = municipality_csv_string
        if activity_level is not None:
            self.activity_level = activity_level
        if activity_level_name is not None:
            self.activity_level_name = activity_level_name
        if danger_type is not None:
            self.danger_type = danger_type
        if danger_type_name is not None:
            self.danger_type_name = danger_type_name
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        if next_warning_time is not None:
            self.next_warning_time = next_warning_time
        if publish_time is not None:
            self.publish_time = publish_time
        if created_time is not None:
            self.created_time = created_time
        if danger_increase_date_time is not None:
            self.danger_increase_date_time = danger_increase_date_time
        if danger_decrease_date_time is not None:
            self.danger_decrease_date_time = danger_decrease_date_time
        if main_text is not None:
            self.main_text = main_text
        if warning_text is not None:
            self.warning_text = warning_text
        if advice_text is not None:
            self.advice_text = advice_text
        if consequence_text is not None:
            self.consequence_text = consequence_text
        if level_meaning_text is not None:
            self.level_meaning_text = level_meaning_text
        if cause_text is not None:
            self.cause_text = cause_text
        if area is not None:
            self.area = area
        if exposed_height_type is not None:
            self.exposed_height_type = exposed_height_type
        if exposed_height_value is not None:
            self.exposed_height_value = exposed_height_value
        if exposed_height_value2 is not None:
            self.exposed_height_value2 = exposed_height_value2
        if exposed_climate_type is not None:
            self.exposed_climate_type = exposed_climate_type
        if cause_list is not None:
            self.cause_list = cause_list
        if micro_blog_post_list is not None:
            self.micro_blog_post_list = micro_blog_post_list
        if station_list is not None:
            self.station_list = station_list

    @property
    def event_id(self):
        """Gets the event_id of this Warning.  # noqa: E501


        :return: The event_id of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Warning.


        :param event_id: The event_id of this Warning.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def id(self):
        """Gets the id of this Warning.  # noqa: E501


        :return: The id of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Warning.


        :param id: The id of this Warning.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def master_id(self):
        """Gets the master_id of this Warning.  # noqa: E501


        :return: The master_id of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        """Sets the master_id of this Warning.


        :param master_id: The master_id of this Warning.  # noqa: E501
        :type: str
        """

        self._master_id = master_id

    @property
    def version(self):
        """Gets the version of this Warning.  # noqa: E501


        :return: The version of this Warning.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Warning.


        :param version: The version of this Warning.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def lang_key(self):
        """Gets the lang_key of this Warning.  # noqa: E501


        :return: The lang_key of this Warning.  # noqa: E501
        :rtype: int
        """
        return self._lang_key

    @lang_key.setter
    def lang_key(self, lang_key):
        """Sets the lang_key of this Warning.


        :param lang_key: The lang_key of this Warning.  # noqa: E501
        :type: int
        """

        self._lang_key = lang_key

    @property
    def cap_status(self):
        """Gets the cap_status of this Warning.  # noqa: E501


        :return: The cap_status of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._cap_status

    @cap_status.setter
    def cap_status(self, cap_status):
        """Sets the cap_status of this Warning.


        :param cap_status: The cap_status of this Warning.  # noqa: E501
        :type: str
        """

        self._cap_status = cap_status

    @property
    def met_id(self):
        """Gets the met_id of this Warning.  # noqa: E501


        :return: The met_id of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._met_id

    @met_id.setter
    def met_id(self, met_id):
        """Sets the met_id of this Warning.


        :param met_id: The met_id of this Warning.  # noqa: E501
        :type: str
        """

        self._met_id = met_id

    @property
    def met_name(self):
        """Gets the met_name of this Warning.  # noqa: E501


        :return: The met_name of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._met_name

    @met_name.setter
    def met_name(self, met_name):
        """Sets the met_name of this Warning.


        :param met_name: The met_name of this Warning.  # noqa: E501
        :type: str
        """

        self._met_name = met_name

    @property
    def county_list(self):
        """Gets the county_list of this Warning.  # noqa: E501


        :return: The county_list of this Warning.  # noqa: E501
        :rtype: list[County]
        """
        return self._county_list

    @county_list.setter
    def county_list(self, county_list):
        """Sets the county_list of this Warning.


        :param county_list: The county_list of this Warning.  # noqa: E501
        :type: list[County]
        """

        self._county_list = county_list

    @property
    def municipality_list(self):
        """Gets the municipality_list of this Warning.  # noqa: E501


        :return: The municipality_list of this Warning.  # noqa: E501
        :rtype: list[Municipality]
        """
        return self._municipality_list

    @municipality_list.setter
    def municipality_list(self, municipality_list):
        """Sets the municipality_list of this Warning.


        :param municipality_list: The municipality_list of this Warning.  # noqa: E501
        :type: list[Municipality]
        """

        self._municipality_list = municipality_list

    @property
    def municipality_csv_string(self):
        """Gets the municipality_csv_string of this Warning.  # noqa: E501


        :return: The municipality_csv_string of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._municipality_csv_string

    @municipality_csv_string.setter
    def municipality_csv_string(self, municipality_csv_string):
        """Sets the municipality_csv_string of this Warning.


        :param municipality_csv_string: The municipality_csv_string of this Warning.  # noqa: E501
        :type: str
        """

        self._municipality_csv_string = municipality_csv_string

    @property
    def activity_level(self):
        """Gets the activity_level of this Warning.  # noqa: E501


        :return: The activity_level of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._activity_level

    @activity_level.setter
    def activity_level(self, activity_level):
        """Sets the activity_level of this Warning.


        :param activity_level: The activity_level of this Warning.  # noqa: E501
        :type: str
        """

        self._activity_level = activity_level

    @property
    def activity_level_name(self):
        """Gets the activity_level_name of this Warning.  # noqa: E501


        :return: The activity_level_name of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._activity_level_name

    @activity_level_name.setter
    def activity_level_name(self, activity_level_name):
        """Sets the activity_level_name of this Warning.


        :param activity_level_name: The activity_level_name of this Warning.  # noqa: E501
        :type: str
        """

        self._activity_level_name = activity_level_name

    @property
    def danger_type(self):
        """Gets the danger_type of this Warning.  # noqa: E501


        :return: The danger_type of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._danger_type

    @danger_type.setter
    def danger_type(self, danger_type):
        """Sets the danger_type of this Warning.


        :param danger_type: The danger_type of this Warning.  # noqa: E501
        :type: str
        """

        self._danger_type = danger_type

    @property
    def danger_type_name(self):
        """Gets the danger_type_name of this Warning.  # noqa: E501


        :return: The danger_type_name of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._danger_type_name

    @danger_type_name.setter
    def danger_type_name(self, danger_type_name):
        """Sets the danger_type_name of this Warning.


        :param danger_type_name: The danger_type_name of this Warning.  # noqa: E501
        :type: str
        """

        self._danger_type_name = danger_type_name

    @property
    def valid_from(self):
        """Gets the valid_from of this Warning.  # noqa: E501


        :return: The valid_from of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this Warning.


        :param valid_from: The valid_from of this Warning.  # noqa: E501
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this Warning.  # noqa: E501


        :return: The valid_to of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this Warning.


        :param valid_to: The valid_to of this Warning.  # noqa: E501
        :type: datetime
        """

        self._valid_to = valid_to

    @property
    def next_warning_time(self):
        """Gets the next_warning_time of this Warning.  # noqa: E501


        :return: The next_warning_time of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._next_warning_time

    @next_warning_time.setter
    def next_warning_time(self, next_warning_time):
        """Sets the next_warning_time of this Warning.


        :param next_warning_time: The next_warning_time of this Warning.  # noqa: E501
        :type: datetime
        """

        self._next_warning_time = next_warning_time

    @property
    def publish_time(self):
        """Gets the publish_time of this Warning.  # noqa: E501


        :return: The publish_time of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this Warning.


        :param publish_time: The publish_time of this Warning.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def created_time(self):
        """Gets the created_time of this Warning.  # noqa: E501


        :return: The created_time of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Warning.


        :param created_time: The created_time of this Warning.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def danger_increase_date_time(self):
        """Gets the danger_increase_date_time of this Warning.  # noqa: E501


        :return: The danger_increase_date_time of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._danger_increase_date_time

    @danger_increase_date_time.setter
    def danger_increase_date_time(self, danger_increase_date_time):
        """Sets the danger_increase_date_time of this Warning.


        :param danger_increase_date_time: The danger_increase_date_time of this Warning.  # noqa: E501
        :type: datetime
        """

        self._danger_increase_date_time = danger_increase_date_time

    @property
    def danger_decrease_date_time(self):
        """Gets the danger_decrease_date_time of this Warning.  # noqa: E501


        :return: The danger_decrease_date_time of this Warning.  # noqa: E501
        :rtype: datetime
        """
        return self._danger_decrease_date_time

    @danger_decrease_date_time.setter
    def danger_decrease_date_time(self, danger_decrease_date_time):
        """Sets the danger_decrease_date_time of this Warning.


        :param danger_decrease_date_time: The danger_decrease_date_time of this Warning.  # noqa: E501
        :type: datetime
        """

        self._danger_decrease_date_time = danger_decrease_date_time

    @property
    def main_text(self):
        """Gets the main_text of this Warning.  # noqa: E501


        :return: The main_text of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._main_text

    @main_text.setter
    def main_text(self, main_text):
        """Sets the main_text of this Warning.


        :param main_text: The main_text of this Warning.  # noqa: E501
        :type: str
        """

        self._main_text = main_text

    @property
    def warning_text(self):
        """Gets the warning_text of this Warning.  # noqa: E501


        :return: The warning_text of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._warning_text

    @warning_text.setter
    def warning_text(self, warning_text):
        """Sets the warning_text of this Warning.


        :param warning_text: The warning_text of this Warning.  # noqa: E501
        :type: str
        """

        self._warning_text = warning_text

    @property
    def advice_text(self):
        """Gets the advice_text of this Warning.  # noqa: E501


        :return: The advice_text of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._advice_text

    @advice_text.setter
    def advice_text(self, advice_text):
        """Sets the advice_text of this Warning.


        :param advice_text: The advice_text of this Warning.  # noqa: E501
        :type: str
        """

        self._advice_text = advice_text

    @property
    def consequence_text(self):
        """Gets the consequence_text of this Warning.  # noqa: E501


        :return: The consequence_text of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._consequence_text

    @consequence_text.setter
    def consequence_text(self, consequence_text):
        """Sets the consequence_text of this Warning.


        :param consequence_text: The consequence_text of this Warning.  # noqa: E501
        :type: str
        """

        self._consequence_text = consequence_text

    @property
    def level_meaning_text(self):
        """Gets the level_meaning_text of this Warning.  # noqa: E501


        :return: The level_meaning_text of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._level_meaning_text

    @level_meaning_text.setter
    def level_meaning_text(self, level_meaning_text):
        """Sets the level_meaning_text of this Warning.


        :param level_meaning_text: The level_meaning_text of this Warning.  # noqa: E501
        :type: str
        """

        self._level_meaning_text = level_meaning_text

    @property
    def cause_text(self):
        """Gets the cause_text of this Warning.  # noqa: E501


        :return: The cause_text of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._cause_text

    @cause_text.setter
    def cause_text(self, cause_text):
        """Sets the cause_text of this Warning.


        :param cause_text: The cause_text of this Warning.  # noqa: E501
        :type: str
        """

        self._cause_text = cause_text

    @property
    def area(self):
        """Gets the area of this Warning.  # noqa: E501


        :return: The area of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Warning.


        :param area: The area of this Warning.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def exposed_height_type(self):
        """Gets the exposed_height_type of this Warning.  # noqa: E501


        :return: The exposed_height_type of this Warning.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_type

    @exposed_height_type.setter
    def exposed_height_type(self, exposed_height_type):
        """Sets the exposed_height_type of this Warning.


        :param exposed_height_type: The exposed_height_type of this Warning.  # noqa: E501
        :type: int
        """

        self._exposed_height_type = exposed_height_type

    @property
    def exposed_height_value(self):
        """Gets the exposed_height_value of this Warning.  # noqa: E501


        :return: The exposed_height_value of this Warning.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_value

    @exposed_height_value.setter
    def exposed_height_value(self, exposed_height_value):
        """Sets the exposed_height_value of this Warning.


        :param exposed_height_value: The exposed_height_value of this Warning.  # noqa: E501
        :type: int
        """

        self._exposed_height_value = exposed_height_value

    @property
    def exposed_height_value2(self):
        """Gets the exposed_height_value2 of this Warning.  # noqa: E501


        :return: The exposed_height_value2 of this Warning.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_value2

    @exposed_height_value2.setter
    def exposed_height_value2(self, exposed_height_value2):
        """Sets the exposed_height_value2 of this Warning.


        :param exposed_height_value2: The exposed_height_value2 of this Warning.  # noqa: E501
        :type: int
        """

        self._exposed_height_value2 = exposed_height_value2

    @property
    def exposed_climate_type(self):
        """Gets the exposed_climate_type of this Warning.  # noqa: E501


        :return: The exposed_climate_type of this Warning.  # noqa: E501
        :rtype: int
        """
        return self._exposed_climate_type

    @exposed_climate_type.setter
    def exposed_climate_type(self, exposed_climate_type):
        """Sets the exposed_climate_type of this Warning.


        :param exposed_climate_type: The exposed_climate_type of this Warning.  # noqa: E501
        :type: int
        """

        self._exposed_climate_type = exposed_climate_type

    @property
    def cause_list(self):
        """Gets the cause_list of this Warning.  # noqa: E501


        :return: The cause_list of this Warning.  # noqa: E501
        :rtype: list[Cause]
        """
        return self._cause_list

    @cause_list.setter
    def cause_list(self, cause_list):
        """Sets the cause_list of this Warning.


        :param cause_list: The cause_list of this Warning.  # noqa: E501
        :type: list[Cause]
        """

        self._cause_list = cause_list

    @property
    def micro_blog_post_list(self):
        """Gets the micro_blog_post_list of this Warning.  # noqa: E501


        :return: The micro_blog_post_list of this Warning.  # noqa: E501
        :rtype: list[MicroBlogPost]
        """
        return self._micro_blog_post_list

    @micro_blog_post_list.setter
    def micro_blog_post_list(self, micro_blog_post_list):
        """Sets the micro_blog_post_list of this Warning.


        :param micro_blog_post_list: The micro_blog_post_list of this Warning.  # noqa: E501
        :type: list[MicroBlogPost]
        """

        self._micro_blog_post_list = micro_blog_post_list

    @property
    def station_list(self):
        """Gets the station_list of this Warning.  # noqa: E501


        :return: The station_list of this Warning.  # noqa: E501
        :rtype: list[Station]
        """
        return self._station_list

    @station_list.setter
    def station_list(self, station_list):
        """Sets the station_list of this Warning.


        :param station_list: The station_list of this Warning.  # noqa: E501
        :type: list[Station]
        """

        self._station_list = station_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Warning, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Warning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
