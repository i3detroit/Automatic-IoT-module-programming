//{} generated on {}
#ifndef _USER_CONFIG_OVERRIDE_H_
#define _USER_CONFIG_OVERRIDE_H_

#if VERSION != 0x06040100
#error "**** WE DO NOT KNOW WHAT VERSION OF TASMOTA IS ****"
#endif

#undef CFG_HOLDER

#undef PROJECT
#undef SAVE_DATA
#undef SAVE_STATE

#undef WIFI_IP_ADDRESS
#undef WIFI_GATEWAY
#undef WIFI_SUBNETMASK
#undef WIFI_DNS

#undef STA_SSID1
#undef STA_PASS1
#undef STA_SSID2
#undef STA_PASS2
#undef WIFI_CONFIG_TOOL
#undef WIFI_CONFIG_NO_SSID

#undef SYS_LOG_HOST
#undef SYS_LOG_PORT
#undef SYS_LOG_LEVEL
#undef SERIAL_LOG_LEVEL
#undef WEB_LOG_LEVEL

#undef OTA_URL

#undef MQTT_USE

#undef MQTT_HOST
#undef MQTT_FINGERPRINT1
#undef MQTT_FINGERPRINT2
#undef MQTT_PORT
#undef MQTT_USER
#undef MQTT_PASS

#undef MQTT_BUTTON_RETAIN
#undef MQTT_POWER_RETAIN
#undef MQTT_SWITCH_RETAIN
#undef MQTT_BUTTON_SWITCH_FORCE_LOCAL

#undef MQTT_STATUS_OFF
#undef MQTT_STATUS_ON
#undef MQTT_CMND_TOGGLE
#undef MQTT_CMND_HOLD

#undef MQTT_FULLTOPIC

#undef SUB_PREFIX
#undef PUB_PREFIX
#undef PUB_PREFIX2
#undef MQTT_TOPIC
#undef MQTT_GRPTOPIC
#undef MQTT_BUTTON_TOPIC
#undef MQTT_SWITCH_TOPIC
#undef MQTT_CLIENT_ID

#undef TELE_PERIOD

#undef DOMOTICZ_UPDATE_TIMER

#undef HOME_ASSISTANT_DISCOVERY_ENABLE

#undef WEB_SERVER
#undef WEB_PASSWORD
#undef FRIENDLY_NAME
#undef EMULATION

#undef NTP_SERVER1
#undef NTP_SERVER2
#undef NTP_SERVER3

#undef TIME_DST_HEMISPHERE
#undef TIME_DST_WEEK
#undef TIME_DST_DAY
#undef TIME_DST_MONTH
#undef TIME_DST_HOUR
#undef TIME_DST_OFFSET

#undef TIME_STD_HEMISPHERE
#undef TIME_STD_WEEK
#undef TIME_STD_DAY
#undef TIME_STD_MONTH
#undef TIME_STD_HOUR
#undef TIME_STD_OFFSET

#undef LATITUDE
#undef LONGITUDE

#undef APP_TIMEZONE
#undef APP_LEDSTATE
#undef APP_PULSETIME
#undef APP_POWERON_STATE
#undef APP_BLINKTIME
#undef APP_BLINKCOUNT
#undef APP_SLEEP

#undef KEY_DEBOUNCE_TIME
#undef KEY_HOLD_TIME
#undef SWITCH_DEBOUNCE_TIME
#undef SWITCH_MODE
#undef WS2812_LEDS

#undef TEMP_CONVERSION
#undef PRESSURE_CONVERSION
#undef TEMP_RESOLUTION
#undef HUMIDITY_RESOLUTION
#undef PRESSURE_RESOLUTION
#undef ENERGY_RESOLUTION
#undef CALC_RESOLUTION

#undef MY_LANGUAGE

#undef WIFI_SOFT_AP_CHANNEL
#undef USE_WPS
#undef USE_SMARTCONFIG

#undef USE_ARDUINO_OTA
#undef MQTT_LIBRARY_TYPE

#undef MQTT_TELE_RETAIN

#undef USE_DOMOTICZ
#undef DOMOTICZ_IN_TOPIC
#undef DOMOTICZ_OUT_TOPIC

#undef USE_HOME_ASSISTANT
#undef HOME_ASSISTANT_DISCOVERY_PREFIX
#undef USE_MQTT_TLS
#undef USE_MQTT_TLS_CA_CERT

#undef USE_KNX
#undef USE_KNX_WEB_MENU

#undef USE_WEBSERVER
#undef WEB_PORT
#undef WEB_USERNAME
#undef USE_EMULATION

#undef USE_DISCOVERY
#undef WEBSERVER_ADVERTISE
#undef MQTT_HOST_DISCOVERY

#undef USE_TIMERS
#undef USE_TIMERS_WEB
#undef USE_SUNRISE
#undef SUNRISE_DAWN_ANGLE

#undef USE_RULES

#undef USE_ADC_VCC

#undef USE_DS18x20_LEGACY
#undef USE_DS18x20
#undef W1_PARASITE_POWER

#undef USE_I2C

#undef USE_SHT
#undef USE_HTU
#undef USE_BMP
#undef USE_BME680
#undef USE_BH1750
#undef USE_VEML6070
#undef USE_VEML6070_RSET
#undef USE_VEML6070_SHOW_RAW
#undef USE_ADS1115
#undef USE_ADS1115_I2CDEV
#undef USE_INA219
#undef USE_SHT3X
#undef USE_TSL2561
#undef USE_MGS
#undef MGS_SENSOR_ADDR
#undef USE_SGP30
#undef USE_SI1145
#undef USE_LM75AD
#undef USE_APDS9960
#undef USE_MCP230xx_ADDR
#undef USE_MCP230xx_ADDR
#undef USE_MCP230xx_OUTPUT
#undef USE_MCP230xx_DISPLAYOUTPUT
#undef USE_PCA9685_ADDR
#undef USE_PCA9685_ADDR
#undef USE_PCA9685_FREQ
#undef USE_MPR121
#undef USE_CCS811
#undef USE_MPU6050
#undef USE_MPU6050_DMP
#undef USE_DS3231
#undef USE_RTC_ADDR
#undef USE_MGC3130

#undef USE_DISPLAY
#undef USE_DISPLAY_MODES1TO5
#undef USE_DISPLAY_LCD
#undef USE_DISPLAY_SSD1306
#undef USE_DISPLAY_MATRIX
#undef MTX_ADDRESS1
#undef MTX_ADDRESS2
#undef MTX_ADDRESS3
#undef MTX_ADDRESS4
#undef MTX_ADDRESS5
#undef MTX_ADDRESS6
#undef MTX_ADDRESS7
#undef MTX_ADDRESS8

#undef USE_SPI

#undef USE_DISPLAY
#undef USE_DISPLAY_ILI9341
#undef USE_DISPLAY_EPAPER_29

#undef USE_MHZ19
#undef USE_SENSEAIR
#undef CO2_LOW
#undef CO2_HIGH
#undef USE_PMS5003
#undef USE_NOVA_SDS
#undef WORKING_PERIOD
#undef USE_SERIAL_BRIDGE
#undef USE_SDM120
#undef SDM120_SPEED
#undef USE_SDM220
#undef USE_SDM630
#undef SDM630_SPEED
#undef USE_MP3_PLAYER
#undef MP3_VOLUME
#undef USE_TUYA_DIMMER
#undef TUYA_DIMMER_ID
#undef USE_ARMTRONIX_DIMMERS
#undef USE_PS_16_DZ
#undef USE_AZ7798

#undef USE_PZEM004T
#undef USE_PZEM_AC
#undef USE_PZEM_DC
#undef USE_MCP39F501

#undef USE_IR_REMOTE
#undef USE_IR_HVAC
#undef USE_IR_RECEIVE
#undef IR_RCV_BUFFER_SIZE
#undef IR_RCV_TIMEOUT
#undef IR_RCV_MIN_UNKNOWN_SIZE

#undef USE_WS2812
#undef USE_WS2812_CTYPE
#undef USE_WS2812_DMA

#undef USE_ARILUX_RF

#undef USE_SR04

#undef USE_TM1638
#undef USE_HX711
#undef USE_HX711_GUI

#undef USE_RF_FLASH

#undef USE_TX20_WIND_SENSOR

#undef USE_RC_SWITCH

#undef USE_RF_SENSOR
#undef USE_THEO_V2
#undef USE_ALECTO_V2

#undef USE_DEBUG_DRIVER

#undef USE_CLASSIC
#undef USE_BASIC
#undef USE_SENSORS
#undef USE_KNX_NO_EMULATION
#undef USE_DISPLAYS
#undef BE_MINIMAL

// force the compiler to show a warning to confirm that this file is inlcuded
#warning "**** user_config_override.h: Using Settings from this File ****"

#define PROJECT                "new-device"          // PROJECT is used as the default topic delimiter
#define SAVE_DATA              1                 // [SaveData] Save changed parameters to Flash (0 = disable, 1 - 3600 seconds)
#define SAVE_STATE             0                 // [SetOption0] Save changed power state to Flash (0 = disable, 1 = enable)

#define WIFI_IP_ADDRESS        "0.0.0.0"         // [IpAddress1] Set to 0.0.0.0 for using DHCP or IP address
#define WIFI_GATEWAY           ""     // [IpAddress2] If not using DHCP set Gateway IP address
#define WIFI_SUBNETMASK        ""   // [IpAddress3] If not using DHCP set Network mask
#define WIFI_DNS               ""     // [IpAddress4] If not using DHCP set DNS IP address (might be equal to WIFI_GATEWAY)

#define WIFI_CONFIG_TOOL       WIFI_RETRY        // [WifiConfig] Default tool if wifi fails to connect
#define WIFI_CONFIG_NO_SSID    WIFI_WPSCONFIG    // Default tool if wifi fails to connect and no SSID is configured

#define SYS_LOG_HOST           ""                // [LogHost] (Linux) syslog host
#define SYS_LOG_PORT           514               // [LogPort] default syslog UDP port
#define SYS_LOG_LEVEL          LOG_LEVEL_NONE    // [SysLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define SERIAL_LOG_LEVEL       LOG_LEVEL_INFO    // [SerialLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define WEB_LOG_LEVEL          LOG_LEVEL_INFO    // [WebLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)

#define OTA_URL ""

#define MQTT_USE               1                 // [SetOption3] Select default MQTT use (0 = Off, 1 = On)

#define MQTT_PORT              1883              // [MqttPort] MQTT port (10123 on CloudMQTT)
#define MQTT_USER              ""       // [MqttUser] MQTT user
#define MQTT_PASS              ""       // [MqttPassword] MQTT password

#define MQTT_BUTTON_RETAIN     0                 // [ButtonRetain] Button may send retain flag (0 = off, 1 = on)
#define MQTT_POWER_RETAIN      0                 // [PowerRetain] Power status message may send retain flag (0 = off, 1 = on)
#define MQTT_SWITCH_RETAIN     0                 // [SwitchRetain] Switch may send retain flag (0 = off, 1 = on)
#define MQTT_BUTTON_SWITCH_FORCE_LOCAL     0     // [SetOption61] Force local operation when button/switch topic is set (0 = off, 1 = on)

#define MQTT_STATUS_OFF        "OFF"             // [StateText1] Command or Status result when turned off (needs to be a string like "0" or "Off")
#define MQTT_STATUS_ON         "ON"              // [StateText2] Command or Status result when turned on (needs to be a string like "1" or "On")
#define MQTT_CMND_TOGGLE       "TOGGLE"          // [StateText3] Command to send when toggling (needs to be a string like "2" or "Toggle")
#define MQTT_CMND_HOLD         "HOLD"            // [StateText4] Command to send when button is kept down for over KEY_HOLD_TIME * 0.1 seconds (needs to be a string like "HOLD")

// %prefix% token options
#define SUB_PREFIX             "cmnd"            // [Prefix1] Sonoff devices subscribe to %prefix%/%topic% being SUB_PREFIX/MQTT_TOPIC and SUB_PREFIX/MQTT_GRPTOPIC
#define PUB_PREFIX             "stat"            // [Prefix2] Sonoff devices publish to %prefix%/%topic% being PUB_PREFIX/MQTT_TOPIC
#define PUB_PREFIX2            "tele"            // [Prefix3] Sonoff devices publish telemetry data to %prefix%/%topic% being PUB_PREFIX2/MQTT_TOPIC/UPTIME, POWER and TIME
                                                 //   May be named the same as PUB_PREFIX
// %topic% token options (also ButtonTopic and SwitchTopic)
#define MQTT_BUTTON_TOPIC      "0"               // [ButtonTopic] MQTT button topic, "0" = same as MQTT_TOPIC, set to 'PROJECT "_BTN_%06X"' for unique topic including device MAC address
#define MQTT_SWITCH_TOPIC      "0"               // [SwitchTopic] MQTT button topic, "0" = same as MQTT_TOPIC, set to 'PROJECT "_SW_%06X"' for unique topic including device MAC address
#define MQTT_CLIENT_ID         "DVES_%06X"       // [MqttClient] Also fall back topic using Chip Id = last 6 characters of MAC address

// -- MQTT - Telemetry ----------------------------
#define TELE_PERIOD            300               // [TelePeriod] Telemetry (0 = disable, 10 - 3600 seconds)

#define DOMOTICZ_UPDATE_TIMER  0                 // [DomoticzUpdateTimer] Send relay status (0 = disable, 1 - 3600 seconds)
#define HOME_ASSISTANT_DISCOVERY_ENABLE   0      // [SetOption19] Home Assistant Discovery (0 = Disable, 1 = Enable)

// -- HTTP ----------------------------------------
#define WEB_SERVER             2                 // [WebServer] Web server (0 = Off, 1 = Start as User, 2 = Start as Admin)
#define WEB_PASSWORD           ""                // [WebPassword] Web server Admin mode Password for WEB_USERNAME (empty string = Disable)
#define EMULATION              EMUL_NONE         // [Emulation] Select Belkin WeMo (single relay/light) or Hue Bridge emulation (multi relay/light) (EMUL_NONE, EMUL_WEMO or EMUL_HUE)

// -- Time - Up to three NTP servers in your region
// we define the first in site config
#define NTP_SERVER2            "nl.pool.ntp.org"    // [NtpServer2] Select second NTP server by name or IP address (5.39.184.5)
#define NTP_SERVER3            "0.nl.pool.ntp.org"  // [NtpServer3] Select third NTP server by name or IP address (93.94.224.67)

// -- Time - Start Daylight Saving Time and timezone offset from UTC in minutes
#define TIME_DST_HEMISPHERE    North             // [TimeDst] Hemisphere (0 or North, 1 or South)
#define TIME_DST_WEEK          Second              // Week of month (0 or Last, 1 or First, 2 or Second, 3 or Third, 4 or Fourth)
#define TIME_DST_DAY           Sun               // Day of week (1 or Sun, 2 or Mon, 3 or Tue, 4 or Wed, 5 or Thu, 6 or Fri, 7 or Sat)
#define TIME_DST_MONTH         Mar               // Month (1 or Jan, 2 or Feb, 3 or Mar, 4 or Apr, 5 or May, 6 or Jun, 7 or Jul, 8 or Aug, 9 or Sep, 10 or Oct, 11 or Nov, 12 or Dec)
#define TIME_DST_HOUR          2                 // Hour (0 to 23)
#define TIME_DST_OFFSET        -240              // Offset from UTC in minutes (-780 to +780)

// -- Time - Start Standard Time and timezone offset from UTC in minutes
#define TIME_STD_HEMISPHERE    North             // [TimeStd] Hemisphere (0 or North, 1 or South)
#define TIME_STD_WEEK          First              // Week of month (0 or Last, 1 or First, 2 or Second, 3 or Third, 4 or Fourth)
#define TIME_STD_DAY           Sun               // Day of week (1 or Sun, 2 or Mon, 3 or Tue, 4 or Wed, 5 or Thu, 6 or Fri, 7 or Sat)
#define TIME_STD_MONTH         Nov               // Month (1 or Jan, 2 or Feb, 3 or Mar, 4 or Apr, 5 or May, 6 or Jun, 7 or Jul, 8 or Aug, 9 or Sep, 10 or Oct, 11 or Nov, 12 or Dec)
#define TIME_STD_HOUR          3                 // Hour (0 to 23)
#define TIME_STD_OFFSET        -300               // Offset from UTC in minutes (-780 to +780)

// -- Application ---------------------------------
#define APP_TIMEZONE           99                 // [Timezone] +1 hour (Amsterdam) (-13 .. 14 = hours from UTC, 99 = use TIME_DST/TIME_STD)
#define APP_LEDSTATE           LED_POWER         // [LedState] Function of led
                                                 //   (LED_OFF, LED_POWER, LED_MQTTSUB, LED_POWER_MQTTSUB, LED_MQTTPUB, LED_POWER_MQTTPUB, LED_MQTT, LED_POWER_MQTT)
#define APP_PULSETIME          0                 // [PulseTime] Time in 0.1 Sec to turn off power for relay 1 (0 = disabled)
#define APP_BLINKTIME          10                // [BlinkTime] Time in 0.1 Sec to blink/toggle power for relay 1
#define APP_BLINKCOUNT         10                // [BlinkCount] Number of blinks (0 = 32000)
#define APP_SLEEP              0                 // [Sleep] Sleep time to lower energy consumption (0 = Off, 1 - 250 mSec)

#define KEY_DEBOUNCE_TIME      50                // [ButtonDebounce] Number of mSeconds button press debounce time
#define KEY_HOLD_TIME          40                // [SetOption32] Number of 0.1 seconds to hold Button or external Pushbutton before sending HOLD message
#define SWITCH_DEBOUNCE_TIME   50                // [SwitchDebounce] Number of mSeconds switch press debounce time
#define SWITCH_MODE            TOGGLE            // [SwitchMode] TOGGLE, FOLLOW, FOLLOW_INV, PUSHBUTTON, PUSHBUTTON_INV, PUSHBUTTONHOLD, PUSHBUTTONHOLD_INV, PUSHBUTTON_TOGGLE (the wall switch state)

#define TEMP_CONVERSION        0                 // [SetOption8] Return temperature in (0 = Celsius or 1 = Fahrenheit)
#define PRESSURE_CONVERSION    0                 // [SetOption24] Return pressure in (0 = hPa or 1 = mmHg)
#define TEMP_RESOLUTION        1                 // [TempRes] Maximum number of decimals (0 - 3) showing sensor Temperature
#define HUMIDITY_RESOLUTION    1                 // [HumRes] Maximum number of decimals (0 - 3) showing sensor Humidity
#define PRESSURE_RESOLUTION    1                 // [PressRes] Maximum number of decimals (0 - 3) showing sensor Pressure
#define ENERGY_RESOLUTION      3                 // [EnergyRes] Maximum number of decimals (0 - 5) showing energy usage in kWh
#define CALC_RESOLUTION        3                 // [CalcRes] Maximum number of decimals (0 - 7) used in commands ADD, SUB, MULT and SCALE

#define WIFI_SOFT_AP_CHANNEL   11                 // Soft Access Point Channel number between 1 and 13 as used by Wifi Manager web GUI
#define MQTT_LIBRARY_TYPE      MQTT_PUBSUBCLIENT   // Use PubSubClient library
#define MQTT_TELE_RETAIN     0                   // Tele messages may send retain flag (0 = off, 1 = on)

#define USE_WEBSERVER                            // Enable web server and Wifi Manager (+66k code, +8k mem)
  #define WEB_PORT             80                // Web server Port for User and Admin mode
  #define WEB_USERNAME         "admin"           // Web server Admin mode user name
#define USE_ADC_VCC                              // Display Vcc in Power status. Disable for use as Analog input on selected devices

#define CFG_HOLDER {}
#define MODULE {}
#define MQTT_GRPTOPIC "{}"
#define MQTT_FULLTOPIC "{}"
#define MQTT_TOPIC "{}"
#define FRIENDLY_NAME "{}"
#define APP_POWERON_STATE {}
{}
{}
#define STA_SSID2 ""
#define STA_PASS2 ""
#endif  // _USER_CONFIG_OVERRIDE_H_
