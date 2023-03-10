#  Copyright (C) 2022  John Scrudato / Gordium Knot Inc. d/b/a OpenSource.Legal
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import enum


class LabelType(str, enum.Enum):
    DOC_TYPE_LABEL = "DOC_TYPE_LABEL"
    TOKEN_LABEL = "TOKEN_LABEL"
    RELATIONSHIP_LABEL = "RELATIONSHIP_LABEL"
    METADATA_LABEL = "METADATA_LABEL"

class SemanticIcon(str, enum.Enum):
    SEARCH = "search"
    MAIL_OUTLINE = "mail outline"
    EXTERNAL = "external"
    SIGNAL = "signal"
    SETTING = "setting"
    HOME = "home"
    INBOX = "inbox"
    BROWSER = "browser"
    TAG = "tag"
    TAGS = "tags"
    CALENDAR = "calendar"
    COMMENT = "comment"
    COMMENTS = "comments"
    SHOP = "shop"
    PRIVACY = "privacy"
    SETTINGS = "settings"
    TROPHY = "trophy"
    PAYMENT = "payment"
    FEED = "feed"
    ALARM_OUTLINE = "alarm outline"
    TASKS = "tasks"
    CLOUD = "cloud"
    LAB = "lab"
    MAIL = "mail"
    IDEA = "idea"
    DASHBOARD = "dashboard"
    SITEMAP = "sitemap"
    ALARM = "alarm"
    TERMINAL = "terminal"
    CODE = "code"
    PROTECT = "protect"
    CALENDAR_OUTLINE = "calendar outline"
    TICKET = "ticket"
    EXTERNAL_SQUARE = "external square"
    MAP = "map"
    BUG = "bug"
    MAIL_SQUARE = "mail square"
    HISTORY = "history"
    OPTIONS = "options"
    COMMENT_OUTLINE = "comment outline"
    COMMENTS_OUTLINE = "comments outline"
    TEXT_TELEPHONE = "text telephone"
    FIND = "find"
    WIFI = "wifi"
    ALARM_SLASH = "alarm slash"
    ALARM_SLASH_OUTLINE = "alarm slash outline"
    COPYRIGHT = "copyright"
    AT = "at"
    EYEDROPPER = "eyedropper"
    PAINT_BRUSH = "paint brush"
    HEARTBEAT = "heartbeat"
    DOWNLOAD = "download"
    REPEAT = "repeat"
    REFRESH = "refresh"
    LOCK = "lock"
    BOOKMARK = "bookmark"
    PRINT = "print"
    WRITE = "write"
    THEME = "theme"
    ADJUST = "adjust"
    EDIT = "edit"
    EXTERNAL_SHARE = "external share"
    BAN = "ban"
    MAIL_FORWARD = "mail forward"
    SHARE = "share"
    EXPAND = "expand"
    COMPRESS = "compress"
    UNHIDE = "unhide"
    HIDE = "hide"
    RANDOM = "random"
    RETWEET = "retweet"
    SIGN_OUT = "sign out"
    PIN = "pin"
    SIGN_IN = "sign in"
    UPLOAD = "upload"
    CALL = "call"
    CALL_SQUARE = "call square"
    REMOVE_BOOKMARK = "remove bookmark"
    UNLOCK = "unlock"
    CONFIGURE = "configure"
    FILTER = "filter"
    WIZARD = "wizard"
    UNDO = "undo"
    EXCHANGE = "exchange"
    CLOUD_DOWNLOAD = "cloud download"
    CLOUD_UPLOAD = "cloud upload"
    REPLY = "reply"
    REPLY_ALL = "reply all"
    ERASE = "erase"
    UNLOCK_ALTERNATE = "unlock alternate"
    ARCHIVE = "archive"
    TRANSLATE = "translate"
    RECYCLE = "recycle"
    SEND = "send"
    SEND_OUTLINE = "send outline"
    SHARE_ALTERNATE = "share alternate"
    SHARE_ALTERNATE_SQUARE = "share alternate square"
    WAIT = "wait"
    WRITE_SQUARE = "write square"
    SHARE_SQUARE = "share square"
    ADD_TO_CART = "add to cart"
    IN_CART = "in cart"
    ADD_USER = "add user"
    REMOVE_USER = "remove user"
    HELP_CIRCLE = "help circle"
    INFO_CIRCLE = "info circle"
    WARNING = "warning"
    WARNING_CIRCLE = "warning circle"
    WARNING_SIGN = "warning sign"
    HELP = "help"
    INFO = "info"
    ANNOUNCEMENT = "announcement"
    BIRTHDAY = "birthday"
    USERS = "users"
    DOCTOR = "doctor"
    CHILD = "child"
    USER = "user"
    HANDICAP = "handicap"
    STUDENT = "student"
    SPY = "spy"
    FEMALE = "female"
    MALE = "male"
    WOMAN = "woman"
    MAN = "man"
    NON_BINARY_TRANSGENDER = "non binary transgender"
    INTERGENDER = "intergender"
    TRANSGENDER = "transgender"
    LESBIAN = "lesbian"
    GAY = "gay"
    HETEROSEXUAL = "heterosexual"
    OTHER_GENDER = "other gender"
    OTHER_GENDER_VERTICAL = "other gender vertical"
    OTHER_GENDER_HORIZONTAL = "other gender horizontal"
    NEUTER = "neuter"
    GRID_LAYOUT = "grid layout"
    LIST_LAYOUT = "list layout"
    BLOCK_LAYOUT = "block layout"
    ZOOM = "zoom"
    ZOOM_OUT = "zoom out"
    RESIZE_VERTICAL = "resize vertical"
    RESIZE_HORIZONTAL = "resize horizontal"
    MAXIMIZE = "maximize"
    CROP = "crop"
    COCKTAIL = "cocktail"
    ROAD = "road"
    FLAG = "flag"
    BOOK = "book"
    GIFT = "gift"
    LEAF = "leaf"
    FIRE = "fire"
    PLANE = "plane"
    MAGNET = "magnet"
    LEGAL = "legal"
    LEMON = "lemon"
    WORLD = "world"
    TRAVEL = "travel"
    SHIPPING = "shipping"
    MONEY = "money"
    LIGHTNING = "lightning"
    RAIN = "rain"
    TREATMENT = "treatment"
    SUITCASE = "suitcase"
    BAR = "bar"
    FLAG_OUTLINE = "flag outline"
    FLAG_CHECKERED = "flag checkered"
    PUZZLE = "puzzle"
    FIRE_EXTINGUISHER = "fire extinguisher"
    ROCKET = "rocket"
    ANCHOR = "anchor"
    BULLSEYE = "bullseye"
    SUN = "sun"
    MOON = "moon"
    FAX = "fax"
    LIFE_RING = "life ring"
    BOMB = "bomb"
    SOCCER = "soccer"
    CALCULATOR = "calculator"
    DIAMOND = "diamond"
    CROSSHAIRS = "crosshairs"
    ASTERISK = "asterisk"
    CERTIFICATE = "certificate"
    CIRCLE = "circle"
    QUOTE_LEFT = "quote left"
    QUOTE_RIGHT = "quote right"
    ELLIPSIS_HORIZONTAL = "ellipsis horizontal"
    ELLIPSIS_VERTICAL = "ellipsis vertical"
    CUBE = "cube"
    CUBES = "cubes"
    CIRCLE_NOTCHED = "circle notched"
    CIRCLE_THIN = "circle thin"
    SQUARE_OUTLINE = "square outline"
    SQUARE = "square"
    CHECKMARK = "checkmark"
    REMOVE = "remove"
    CHECKMARK_BOX = "checkmark box"
    MOVE = "move"
    ADD_CIRCLE = "add circle"
    MINUS_CIRCLE = "minus circle"
    REMOVE_CIRCLE = "remove circle"
    CHECK_CIRCLE = "check circle"
    REMOVE_CIRCLE_OUTLINE = "remove circle outline"
    CHECK_CIRCLE_OUTLINE = "check circle outline"
    PLUS = "plus"
    MINUS = "minus"
    ADD_SQUARE = "add square"
    RADIO = "radio"
    SELECTED_RADIO = "selected radio"
    MINUS_SQUARE = "minus square"
    MINUS_SQUARE_OUTLINE = "minus square outline"
    CHECK_SQUARE = "check square"
    PLUS_SQUARE_OUTLINE = "plus square outline"
    TOGGLE_OFF = "toggle off"
    TOGGLE_ON = "toggle on"
    FILM = "film"
    SOUND = "sound"
    PHOTO = "photo"
    BAR_CHART = "bar chart"
    CAMERA_RETRO = "camera retro"
    NEWSPAPER = "newspaper"
    AREA_CHART = "area chart"
    PIE_CHART = "pie chart"
    LINE_CHART = "line chart"
    ARROW_CIRCLE_OUTLINE_DOWN = "arrow circle outline down"
    ARROW_CIRCLE_OUTLINE_UP = "arrow circle outline up"
    CHEVRON_LEFT = "chevron left"
    CHEVRON_RIGHT = "chevron right"
    ARROW_LEFT = "arrow left"
    ARROW_RIGHT = "arrow right"
    ARROW_UP = "arrow up"
    ARROW_DOWN = "arrow down"
    CHEVRON_UP = "chevron up"
    CHEVRON_DOWN = "chevron down"
    POINTING_RIGHT = "pointing right"
    POINTING_LEFT = "pointing left"
    POINTING_UP = "pointing up"
    POINTING_DOWN = "pointing down"
    ARROW_CIRCLE_LEFT = "arrow circle left"
    ARROW_CIRCLE_RIGHT = "arrow circle right"
    ARROW_CIRCLE_UP = "arrow circle up"
    ARROW_CIRCLE_DOWN = "arrow circle down"
    CARET_DOWN = "caret down"
    CARET_UP = "caret up"
    CARET_LEFT = "caret left"
    CARET_RIGHT = "caret right"
    ANGLE_DOUBLE_LEFT = "angle double left"
    ANGLE_DOUBLE_RIGHT = "angle double right"
    ANGLE_DOUBLE_UP = "angle double up"
    ANGLE_DOUBLE_DOWN = "angle double down"
    ANGLE_LEFT = "angle left"
    ANGLE_RIGHT = "angle right"
    ANGLE_UP = "angle up"
    ANGLE_DOWN = "angle down"
    CHEVRON_CIRCLE_LEFT = "chevron circle left"
    CHEVRON_CIRCLE_RIGHT = "chevron circle right"
    CHEVRON_CIRCLE_UP = "chevron circle up"
    CHEVRON_CIRCLE_DOWN = "chevron circle down"
    TOGGLE_DOWN = "toggle down"
    TOGGLE_UP = "toggle up"
    TOGGLE_RIGHT = "toggle right"
    LONG_ARROW_DOWN = "long arrow down"
    LONG_ARROW_UP = "long arrow up"
    LONG_ARROW_LEFT = "long arrow left"
    LONG_ARROW_RIGHT = "long arrow right"
    ARROW_CIRCLE_OUTLINE_RIGHT = "arrow circle outline right"
    ARROW_CIRCLE_OUTLINE_LEFT = "arrow circle outline left"
    TOGGLE_LEFT = "toggle left"
    POWER = "power"
    TRASH = "trash"
    TRASH_OUTLINE = "trash outline"
    DISK_OUTLINE = "disk outline"
    DESKTOP = "desktop"
    LAPTOP = "laptop"
    TABLET = "tablet"
    MOBILE = "mobile"
    GAME = "game"
    KEYBOARD = "keyboard"
    PLUG = "plug"
    FOLDER = "folder"
    FOLDER_OPEN = "folder open"
    LEVEL_UP = "level up"
    LEVEL_DOWN = "level down"
    FILE = "file"
    FILE_OUTLINE = "file outline"
    FILE_TEXT = "file text"
    FILE_TEXT_OUTLINE = "file text outline"
    FOLDER_OUTLINE = "folder outline"
    FOLDER_OPEN_OUTLINE = "folder open outline"
    FILE_PDF_OUTLINE = "file pdf outline"
    FILE_WORD_OUTLINE = "file word outline"
    FILE_EXCEL_OUTLINE = "file excel outline"
    FILE_POWERPOINT_OUTLINE = "file powerpoint outline"
    FILE_IMAGE_OUTLINE = "file image outline"
    FILE_ARCHIVE_OUTLINE = "file archive outline"
    FILE_AUDIO_OUTLINE = "file audio outline"
    FILE_VIDEO_OUTLINE = "file video outline"
    FILE_CODE_OUTLINE = "file code outline"
    BARCODE = "barcode"
    QRCODE = "qrcode"
    FORK = "fork"
    HTML5 = "html5"
    CSS3 = "css3"
    RSS = "rss"
    RSS_SQUARE = "rss square"
    OPENID = "openid"
    DATABASE = "database"
    SERVER = "server"
    HEART = "heart"
    STAR = "star"
    EMPTY_STAR = "empty star"
    THUMBS_OUTLINE_UP = "thumbs outline up"
    THUMBS_OUTLINE_DOWN = "thumbs outline down"
    STAR_HALF = "star half"
    EMPTY_HEART = "empty heart"
    SMILE = "smile"
    FROWN = "frown"
    MEH = "meh"
    STAR_HALF_EMPTY = "star half empty"
    THUMBS_UP = "thumbs up"
    THUMBS_DOWN = "thumbs down"
    MUSIC = "music"
    VIDEO_PLAY_OUTLINE = "video play outline"
    VOLUME_OFF = "volume off"
    VOLUME_DOWN = "volume down"
    VOLUME_UP = "volume up"
    RECORD = "record"
    STEP_BACKWARD = "step backward"
    FAST_BACKWARD = "fast backward"
    BACKWARD = "backward"
    PLAY = "play"
    PAUSE = "pause"
    STOP = "stop"
    FORWARD = "forward"
    FAST_FORWARD = "fast forward"
    STEP_FORWARD = "step forward"
    EJECT = "eject"
    UNMUTE = "unmute"
    MUTE = "mute"
    VIDEO_PLAY = "video play"
    CLOSED_CAPTIONING = "closed captioning"
    MARKER = "marker"
    COFFEE = "coffee"
    FOOD = "food"
    BUILDING_OUTLINE = "building outline"
    HOSPITAL = "hospital"
    EMERGENCY = "emergency"
    FIRST_AID = "first aid"
    MILITARY = "military"
    H = "h"
    LOCATION_ARROW = "location arrow"
    SPACE_SHUTTLE = "space shuttle"
    UNIVERSITY = "university"
    BUILDING = "building"
    PAW = "paw"
    SPOON = "spoon"
    CAR = "car"
    TAXI = "taxi"
    TREE = "tree"
    BICYCLE = "bicycle"
    BUS = "bus"
    SHIP = "ship"
    MOTORCYCLE = "motorcycle"
    STREET_VIEW = "street view"
    HOTEL = "hotel"
    TRAIN = "train"
    SUBWAY = "subway"
    TABLE = "table"
    COLUMNS = "columns"
    SORT = "sort"
    SORT_ASCENDING = "sort ascending"
    SORT_DESCENDING = "sort descending"
    SORT_ALPHABET_ASCENDING = "sort alphabet ascending"
    SORT_ALPHABET_DESCENDING = "sort alphabet descending"
    SORT_CONTENT_ASCENDING = "sort content ascending"
    SORT_CONTENT_DESCENDING = "sort content descending"
    SORT_NUMERIC_ASCENDING = "sort numeric ascending"
    SORT_NUMERIC_DESCENDING = "sort numeric descending"
    FONT = "font"
    BOLD = "bold"
    ITALIC = "italic"
    TEXT_HEIGHT = "text height"
    TEXT_WIDTH = "text width"
    ALIGN_LEFT = "align left"
    ALIGN_CENTER = "align center"
    ALIGN_RIGHT = "align right"
    ALIGN_JUSTIFY = "align justify"
    LIST = "list"
    OUTDENT = "outdent"
    INDENT = "indent"
    LINKIFY = "linkify"
    CUT = "cut"
    COPY = "copy"
    ATTACH = "attach"
    SAVE = "save"
    CONTENT = "content"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"
    STRIKETHROUGH = "strikethrough"
    UNDERLINE = "underline"
    PASTE = "paste"
    UNLINK = "unlink"
    SUPERSCRIPT = "superscript"
    SUBSCRIPT = "subscript"
    HEADER = "header"
    PARAGRAPH = "paragraph"
    EURO = "euro"
    POUND = "pound"
    DOLLAR = "dollar"
    RUPEE = "rupee"
    YEN = "yen"
    RUBLE = "ruble"
    WON = "won"
    LIRA = "lira"
    SHEKEL = "shekel"
    PAYPAL = "paypal"
    PAYPAL_CARD = "paypal card"
    GOOGLE_WALLET = "google wallet"
    VISA = "visa"
    MASTERCARD = "mastercard"
    DISCOVER = "discover"
    AMERICAN_EXPRESS = "american express"
    STRIPE = "stripe"
    TWITTER_SQUARE = "twitter square"
    FACEBOOK_SQUARE = "facebook square"
    LINKEDIN_SQUARE = "linkedin square"
    GITHUB_SQUARE = "github square"
    TWITTER = "twitter"
    FACEBOOK = "facebook"
    GITHUB = "github"
    PINTEREST = "pinterest"
    PINTEREST_SQUARE = "pinterest square"
    GOOGLE_PLUS_SQUARE = "google plus square"
    GOOGLE_PLUS = "google plus"
    LINKEDIN = "linkedin"
    GITHUB_ALTERNATE = "github alternate"
    MAXCDN = "maxcdn"
    BITCOIN = "bitcoin"
    YOUTUBE_SQUARE = "youtube square"
    YOUTUBE = "youtube"
    XING = "xing"
    XING_SQUARE = "xing square"
    YOUTUBE_PLAY = "youtube play"
    DROPBOX = "dropbox"
    STACK_OVERFLOW = "stack overflow"
    INSTAGRAM = "instagram"
    FLICKR = "flickr"
    ADN = "adn"
    BITBUCKET = "bitbucket"
    BITBUCKET_SQUARE = "bitbucket square"
    TUMBLR = "tumblr"
    TUMBLR_SQUARE = "tumblr square"
    APPLE = "apple"
    WINDOWS = "windows"
    ANDROID = "android"
    LINUX = "linux"
    DRIBBBLE = "dribbble"
    SKYPE = "skype"
    FOURSQUARE = "foursquare"
    TRELLO = "trello"
    GITTIP = "gittip"
    VK = "vk"
    WEIBO = "weibo"
    RENREN = "renren"
    PAGELINES = "pagelines"
    STACK_EXCHANGE = "stack exchange"
    VIMEO = "vimeo"
    SLACK = "slack"
    WORDPRESS = "wordpress"
    YAHOO = "yahoo"
    GOOGLE = "google"
    REDDIT = "reddit"
    REDDIT_SQUARE = "reddit square"
    STUMBLEUPON_CIRCLE = "stumbleupon circle"
    STUMBLEUPON = "stumbleupon"
    DELICIOUS = "delicious"
    DIGG = "digg"
    PIED_PIPER = "pied piper"
    PIED_PIPER_ALTERNATE = "pied piper alternate"
    DRUPAL = "drupal"
    JOOMLA = "joomla"
    BEHANCE = "behance"
    BEHANCE_SQUARE = "behance square"
    STEAM = "steam"
    STEAM_SQUARE = "steam square"
    SPOTIFY = "spotify"
    DEVIANTART = "deviantart"
    SOUNDCLOUD = "soundcloud"
    VINE = "vine"
    CODEPEN = "codepen"
    JSFIDDLE = "jsfiddle"
    REBEL = "rebel"
    EMPIRE = "empire"
    GIT_SQUARE = "git square"
    GIT = "git"
    HACKER_NEWS = "hacker news"
    TENCENT_WEIBO = "tencent weibo"
    QQ = "qq"
    WECHAT = "wechat"
    SLIDESHARE = "slideshare"
    TWITCH = "twitch"
    YELP = "yelp"
    LASTFM = "lastfm"
    LASTFM_SQUARE = "lastfm square"
    IOXHOST = "ioxhost"
    ANGELLIST = "angellist"
    MEANPATH = "meanpath"
    BUYSELLADS = "buysellads"
    CONNECTDEVELOP = "connectdevelop"
    DASHCUBE = "dashcube"
    FORUMBEE = "forumbee"
    LEANPUB = "leanpub"
    SELLSY = "sellsy"
    SHIRTSINBULK = "shirtsinbulk"
    SIMPLYBUILT = "simplybuilt"
    SKYATLAS = "skyatlas"
    WHATSAPP = "whatsapp"
    VIACOIN = "viacoin"
    MEDIUM = "medium"
    LIKE = "like"
    FAVORITE = "favorite"
    VIDEO = "video"
    CHECK = "check"
    CLOSE = "close"
    CANCEL = "cancel"
    DELETE = "delete"
    X = "x"
    USER_TIMES = "user times"
    USER_CLOSE = "user close"
    USER_CANCEL = "user cancel"
    USER_DELETE = "user delete"
    USER_X = "user x"
    ZOOM_IN = "zoom in"
    MAGNIFY = "magnify"
    SHUTDOWN = "shutdown"
    CLOCK = "clock"
    TIME = "time"
    PLAY_CIRCLE_OUTLINE = "play circle outline"
    HEADPHONE = "headphone"
    CAMERA = "camera"
    VIDEO_CAMERA = "video camera"
    PICTURE = "picture"
    PENCIL = "pencil"
    COMPOSE = "compose"
    POINT = "point"
    TINT = "tint"
    SIGNUP = "signup"
    PLUS_CIRCLE = "plus circle"
    DONT = "dont"
    MINIMIZE = "minimize"
    ADD = "add"
    EYE = "eye"
    ATTENTION = "attention"
    CART = "cart"
    SHUFFLE = "shuffle"
    TALK = "talk"
    CHAT = "chat"
    SHOPPING_CART = "shopping cart"
    BAR_GRAPH = "bar graph"
    AREA_GRAPH = "area graph"
    PIE_GRAPH = "pie graph"
    LINE_GRAPH = "line graph"
    KEY = "key"
    COGS = "cogs"
    DISCUSSIONS = "discussions"
    LIKE_OUTLINE = "like outline"
    DISLIKE_OUTLINE = "dislike outline"
    HEART_OUTLINE = "heart outline"
    LOG_OUT = "log out"
    THUMB_TACK = "thumb tack"
    WINNER = "winner"
    BOOKMARK_OUTLINE = "bookmark outline"
    PHONE = "phone"
    PHONE_SQUARE = "phone square"
    CREDIT_CARD = "credit card"
    HDD_OUTLINE = "hdd outline"
    BULLHORN = "bullhorn"
    BELL = "bell"
    BELL_OUTLINE = "bell outline"
    BELL_SLASH = "bell slash"
    BELL_SLASH_OUTLINE = "bell slash outline"
    HAND_OUTLINE_RIGHT = "hand outline right"
    HAND_OUTLINE_LEFT = "hand outline left"
    HAND_OUTLINE_UP = "hand outline up"
    HAND_OUTLINE_DOWN = "hand outline down"
    GLOBE = "globe"
    WRENCH = "wrench"
    BRIEFCASE = "briefcase"
    GROUP = "group"
    FLASK = "flask"
    SIDEBAR = "sidebar"
    BARS = "bars"
    LIST_UL = "list ul"
    LIST_OL = "list ol"
    NUMBERED_LIST = "numbered list"
    MAGIC = "magic"
    TRUCK = "truck"
    CURRENCY = "currency"
    TRIANGLE_DOWN = "triangle down"
    DROPDOWN = "dropdown"
    TRIANGLE_UP = "triangle up"
    TRIANGLE_LEFT = "triangle left"
    TRIANGLE_RIGHT = "triangle right"
    ENVELOPE = "envelope"
    CONVERSATION = "conversation"
    UMBRELLA = "umbrella"
    CLIPBOARD = "clipboard"
    LIGHTBULB = "lightbulb"
    AMBULANCE = "ambulance"
    MEDKIT = "medkit"
    FIGHTER_JET = "fighter jet"
    BEER = "beer"
    PLUS_SQUARE = "plus square"
    COMPUTER = "computer"
    CIRCLE_OUTLINE = "circle outline"
    INTERSEX = "intersex"
    ASEXUAL = "asexual"
    SPINNER = "spinner"
    GAMEPAD = "gamepad"
    STAR_HALF_FULL = "star half full"
    QUESTION = "question"
    ERASER = "eraser"
    MICROPHONE = "microphone"
    MICROPHONE_SLASH = "microphone slash"
    SHIELD = "shield"
    TARGET = "target"
    PLAY_CIRCLE = "play circle"
    PENCIL_SQUARE = "pencil square"
    COMPASS = "compass"
    AMEX = "amex"
    EUR = "eur"
    GBP = "gbp"
    USD = "usd"
    INR = "inr"
    CNY = "cny"
    RMB = "rmb"
    JPY = "jpy"
    ROUBLE = "rouble"
    RUB = "rub"
    KRW = "krw"
    BTC = "btc"
    SHEQEL = "sheqel"
    ILS = "ils"
    TRY = "try"
    ZIP = "zip"
    DOT_CIRCLE_OUTLINE = "dot circle outline"
    SLIDERS = "sliders"
    WI_FI = "wi-fi"
    GRADUATION = "graduation"
    WEIXIN = "weixin"
    BINOCULARS = "binoculars"
    GRATIPAY = "gratipay"
    GENDERLESS = "genderless"
    TELETYPE = "teletype"
    POWER_CORD = "power cord"
    TTY = "tty"
    CC = "cc"
    PLUS_CART = "plus cart"
    ARROW_DOWN_CART = "arrow down cart"
    DETECTIVE = "detective"
    VENUS = "venus"
    MARS = "mars"
    MERCURY = "mercury"
    VENUS_DOUBLE = "venus double"
    FEMALE_HOMOSEXUAL = "female homosexual"
    MARS_DOUBLE = "mars double"
    MALE_HOMOSEXUAL = "male homosexual"
    VENUS_MARS = "venus mars"
    MARS_STROKE = "mars stroke"
    MARS_ALTERNATE = "mars alternate"
    MARS_VERTICAL = "mars vertical"
    MARS_HORIZONTAL = "mars horizontal"
    MARS_STROKE_VERTICAL = "mars stroke vertical"
    MARS_STROKE_HORIZONTAL = "mars stroke horizontal"
    FACEBOOK_OFFICIAL = "facebook official"
    PINTEREST_OFFICIAL = "pinterest official"
    BED = "bed"
