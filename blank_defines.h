//generate undefines:
//grep "#define" ../Tasmota/tasmota/my_user_config.h | grep -v _MY_USER_CONFIG_H_ | sed 's/.*define \([A-Z_0-9]*\).*/#undef \1/' | sort | uniq | tee -a blank_defines.h
//Config for {name} generated on {datetime}
#ifndef _USER_CONFIG_OVERRIDE_H_
#define _USER_CONFIG_OVERRIDE_H_

#undef APP_BLINKCOUNT
#undef APP_BLINKTIME
#undef APP_LEDMASK
#undef APP_LEDSTATE
#undef APP_POWERON_STATE
#undef APP_PULSETIME
#undef APP_SLEEP
#undef APP_TIMEZONE
#undef BOOT_LOOP_OFFSET
#undef CALC_RESOLUTION
#undef CFG_HOLDER
#undef CO2_HIGH
#undef CO2_LOW
#undef COLOR_BACKGROUND
#undef COLOR_BUTTON
#undef COLOR_BUTTON_HOVER
#undef COLOR_BUTTON_RESET
#undef COLOR_BUTTON_RESET_HOVER
#undef COLOR_BUTTON_SAVE
#undef COLOR_BUTTON_SAVE_HOVER
#undef COLOR_BUTTON_TEXT
#undef COLOR_CONSOLE
#undef COLOR_CONSOLE_TEXT
#undef COLOR_FORM
#undef COLOR_INPUT
#undef COLOR_INPUT_TEXT
#undef COLOR_TEXT
#undef COLOR_TEXT_SUCCESS
#undef COLOR_TEXT_WARNING
#undef COLOR_TIMER_TAB_BACKGROUND
#undef COLOR_TIMER_TAB_TEXT
#undef COLOR_TITLE_TEXT
#undef CORS_DOMAIN
#undef DDS2382_SPEED
#undef DDSU666_SPEED
#undef DEBUG_TASMOTA_CORE
#undef DEBUG_TASMOTA_DRIVER
#undef DEBUG_TASMOTA_SENSOR
#undef DOMOTICZ_IN_TOPIC
#undef DOMOTICZ_OUT_TOPIC
#undef DOMOTICZ_UPDATE_TIMER
#undef EMULATION
#undef ENERGY_RESOLUTION
#undef EXS_MCU_CMNDS
#undef FIRMWARE_DISPLAYS
#undef FIRMWARE_IR
#undef FIRMWARE_IR_CUSTOM
#undef FIRMWARE_KNX_NO_EMULATION
#undef FIRMWARE_LITE
#undef FIRMWARE_MINIMAL
#undef FIRMWARE_SENSORS
#undef FRIENDLY_NAME
#undef HOME_ASSISTANT_DISCOVERY_ENABLE
#undef HOME_ASSISTANT_DISCOVERY_PREFIX
#undef HUMIDITY_RESOLUTION
#undef IR_RCV_BUFFER_SIZE
#undef IR_RCV_MIN_UNKNOWN_SIZE
#undef IR_RCV_TIMEOUT
#undef KEY_DEBOUNCE_TIME
#undef KEY_HOLD_TIME
#undef LATITUDE
#undef LONGITUDE
#undef MAX31865_PTD_BIAS
#undef MAX31865_PTD_RES
#undef MAX31865_PTD_WIRES
#undef MAX31865_REF_RES
#undef MDNS_ENABLED
#undef MGS_SENSOR_ADDR
#undef MODULE
#undef MP3_VOLUME
#undef MQTT_BUTTON_RETAIN
#undef MQTT_BUTTON_SWITCH_FORCE_LOCAL
#undef MQTT_BUTTON_TOPIC
#undef MQTT_CLEAN_SESSION
#undef MQTT_CLIENT_ID
#undef MQTT_CMND_HOLD
#undef MQTT_CMND_TOGGLE
#undef MQTT_FINGERPRINT1
#undef MQTT_FINGERPRINT2
#undef MQTT_FULLTOPIC
#undef MQTT_GRPTOPIC
#undef MQTT_HOST
#undef MQTT_HOST_DISCOVERY
#undef MQTT_LOG_LEVEL
#undef MQTT_PASS
#undef MQTT_PORT
#undef MQTT_POWER_RETAIN
#undef MQTT_STATUS_OFF
#undef MQTT_STATUS_ON
#undef MQTT_SWITCH_RETAIN
#undef MQTT_SWITCH_TOPIC
#undef MQTT_TELE_RETAIN
#undef MQTT_TOPIC
#undef MQTT_USE
#undef MQTT_USER
#undef MTX_ADDRESS1
#undef MTX_ADDRESS2
#undef MTX_ADDRESS3
#undef MTX_ADDRESS4
#undef MTX_ADDRESS5
#undef MTX_ADDRESS6
#undef MTX_ADDRESS7
#undef MTX_ADDRESS8
#undef MY_LANGUAGE
#undef NTP_SERVER1
#undef NTP_SERVER2
#undef NTP_SERVER3
#undef OTA_URL
#undef PMS_MODEL_PMS3003
#undef PRESSURE_CONVERSION
#undef PRESSURE_RESOLUTION
#undef PROJECT
#undef PUB_PREFIX
#undef PUB_PREFIX2
#undef PWM_MAX_SLEEP
#undef ROTARY_V1
#undef SAVE_DATA
#undef SAVE_STATE
#undef SDM120_SPEED
#undef SDM630_SPEED
#undef SERIAL_LOG_LEVEL
#undef SOLAXX1_PV2
#undef SOLAXX1_SPEED
#undef STA_PASS1
#undef STA_PASS2
#undef STARTING_OFFSET
#undef STA_SSID1
#undef STA_SSID2
#undef SUB_PREFIX
#undef SUNRISE_DAWN_ANGLE
#undef SUPPORT_IF_STATEMENT
#undef SUPPORT_MQTT_EVENT
#undef SWITCH_DEBOUNCE_TIME
#undef SWITCH_MODE
#undef SYS_LOG_HOST
#undef SYS_LOG_LEVEL
#undef SYS_LOG_PORT
#undef TELE_ON_POWER
#undef TELE_PERIOD
#undef TEMP_CONVERSION
#undef TEMP_RESOLUTION
#undef TIME_DST_DAY
#undef TIME_DST_HEMISPHERE
#undef TIME_DST_HOUR
#undef TIME_DST_MONTH
#undef TIME_DST_OFFSET
#undef TIME_DST_WEEK
#undef TIME_STD_DAY
#undef TIME_STD_HEMISPHERE
#undef TIME_STD_HOUR
#undef TIME_STD_MONTH
#undef TIME_STD_OFFSET
#undef TIME_STD_WEEK
#undef TUYA_DIMMER_ID
#undef USE_4K_RSA
#undef USE_A4988_STEPPER
#undef USE_ADC_VCC
#undef USE_ADE7953
#undef USE_ADS1115
#undef USE_ALECTO_V2
#undef USE_APDS9960
#undef USE_ARDUINO_OTA
#undef USE_ARILUX_RF
#undef USE_ARMTRONIX_DIMMERS
#undef USE_AZ7798
#undef USE_BH1750
#undef USE_BME680
#undef USE_BMP
#undef USE_BUZZER
#undef USE_CCS811
#undef USE_CHIRP
#undef USE_CONFIG_OVERRIDE
#undef USE_COUNTER
#undef USE_DDS2382
#undef USE_DDSU666
#undef USE_DEBUG_DRIVER
#undef USE_DEEPSLEEP
#undef USE_DHT
#undef USE_DHT12
#undef USE_DISCOVERY
#undef USE_DISPLAY
#undef USE_DISPLAY_EPAPER_29
#undef USE_DISPLAY_EPAPER_42
#undef USE_DISPLAY_ILI9341
#undef USE_DISPLAY_ILI9488
#undef USE_DISPLAY_LCD
#undef USE_DISPLAY_MATRIX
#undef USE_DISPLAY_MODES1TO5
#undef USE_DISPLAY_RA8876
#undef USE_DISPLAY_SH1106
#undef USE_DISPLAY_SSD1306
#undef USE_DISPLAY_SSD1351
#undef USE_DOMOTICZ
#undef USE_DS18
#undef USE_DS3231
#undef USE_EMULATION_HUE
#undef USE_EMULATION_WEMO
#undef USE_ENERGY_MARGIN_DETECTION
#undef USE_ENERGY_POWER_LIMIT
#undef USE_EXPRESSION
#undef USE_EXS_DIMMER
#undef USE_FLOG
#undef USE_GPS
#undef USE_HIH6
#undef USE_HOME_ASSISTANT
#undef USE_HPMA
#undef USE_HRE
#undef USE_HTU
#undef USE_HX711
#undef USE_HX711_GUI
#undef USE_I2C
#undef USE_IBEACON
#undef USE_INA219
#undef USE_INA226
#undef USE_IR_RECEIVE
#undef USE_IR_REMOTE
#undef USE_IR_SEND_NEC
#undef USE_IR_SEND_RC5
#undef USE_IR_SEND_RC6
#undef USE_JAVASCRIPT_ES6
#undef USE_KNX
#undef USE_KNX_WEB_MENU
#undef USE_LM75AD
#undef USE_MAX31855
#undef USE_MAX31865
#undef USE_MAX44009
#undef USE_MCP230
#undef USE_MCP39F501
#undef USE_MGC3130
#undef USE_MGS
#undef USE_MHZ19
#undef USE_MLX90614
#undef USE_MP3_PLAYER
#undef USE_MPR121
#undef USE_MPU6050
#undef USE_MPU6050_DMP
#undef USE_MQTT_AWS_IOT
#undef USE_MQTT_TLS
#undef USE_MQTT_TLS_CA_CERT
#undef USE_MQTT_TLS_FORCE_EC_CIPHER
#undef USE_MY92X1
#undef USE_NOVA_SDS
#undef USE_PAJ7620
#undef USE_PCA9685_ADDR
#undef USE_PCA9685_FREQ
#undef USE_PCF8574
#undef USE_PMS5003
#undef USE_PN532_CAUSE_EVENTS
#undef USE_PN532_DATA_FUNCTION
#undef USE_PN532_DATA_RAW
#undef USE_PN532_HSU
#undef USE_PS_16_DZ
#undef USE_PZEM004T
#undef USE_PZEM_AC
#undef USE_PZEM_DC
#undef USE_RC_SWITCH
#undef USE_RDM6300
#undef USE_RF_FLASH
#undef USE_RF_SENSOR
#undef USE_RTC_ADDR
#undef USE_RULES
#undef USE_SCD30
#undef USE_SCRIPT
#undef USE_SCRIPT_FATFS
#undef USE_SDM120
#undef USE_SDM630
#undef USE_SENSEAIR
#undef USE_SERIAL_BRIDGE
#undef USE_SGP30
#undef USE_SHT
#undef USE_SHT3X
#undef USE_SHUTTER
#undef USE_SI1145
#undef USE_SM16716
#undef USE_SM2135
#undef USE_SOLAX_X1
#undef USE_SONOFF_IFAN
#undef USE_SONOFF_L1
#undef USE_SONOFF_RF
#undef USE_SONOFF_SC
#undef USE_SPI
#undef USE_SPS30
#undef USE_SR04
#undef USE_SUNRISE
#undef USE_TASMOTA_SLAVE
#undef USE_TASMOTA_SLAVE_FLASH_SPEED
#undef USE_TASMOTA_SLAVE_SERIAL_SPEED
#undef USE_THEO_V2
#undef USE_TIMERS
#undef USE_TIMERS_WEB
#undef USE_TM1638
#undef USE_TSL2561
#undef USE_TSL2591
#undef USE_TUYA_MCU
#undef USE_TX20_WIND_SENSOR
#undef USE_VEML6070
#undef USE_VEML6070_RSET
#undef USE_VEML6070_SHOW_RAW
#undef USE_VL53L0X
#undef USE_WEBSEND_RESPONSE
#undef USE_WEBSERVER
#undef USE_WS2812
#undef USE_WS2812_CTYPE
#undef USE_WS2812_DMA
#undef USE_WS2812_HARDWARE
#undef USE_ZIGBEE
#undef USE_ZIGBEE_CHANNEL
#undef USE_ZIGBEE_COALESCE_ATTR_TIMER
#undef USE_ZIGBEE_EXTPANID
#undef USE_ZIGBEE_PANID
#undef USE_ZIGBEE_PERMIT_JOIN
#undef USE_ZIGBEE_PRECFGKEY_H
#undef USE_ZIGBEE_PRECFGKEY_L
#undef W1_PARASITE_POWER
#undef WEB_LOG_LEVEL
#undef WEB_PASSWORD
#undef WEB_PORT
#undef WEB_SERVER
#undef WEBSERVER_ADVERTISE
#undef WEB_USERNAME
#undef WIFI_CONFIG_TOOL
#undef WIFI_DNS
#undef WIFI_GATEWAY
#undef WIFI_IP_ADDRESS
#undef WIFI_SOFT_AP_CHANNEL
#undef WIFI_SUBNETMASK
#undef WS2812_LEDS

// force the compiler to show a warning to confirm that this file is inlcuded
#warning "**** user_config_override.h: Using Settings from this File ****"

// -- Project -------------------------------------
#define PROJECT                "tasmota"         // PROJECT is used as the default topic delimiter

// If not selected the default will be SONOFF_BASIC
//#define MODULE                 SONOFF_BASIC      // [Module] Select default model from tasmota_template.h

#define SAVE_DATA              1                 // [SaveData] Save changed parameters to Flash (0 = disable, 1 - 3600 seconds)
#define SAVE_STATE             1                 // [SetOption0] Save changed power state to Flash (0 = disable, 1 = enable)
#define BOOT_LOOP_OFFSET       1                 // [SetOption36] Number of boot loops before starting restoring defaults (0 = disable, 1..200 = boot loops offset)

// -- Wifi ----------------------------------------
#define WIFI_IP_ADDRESS        "0.0.0.0"         // [IpAddress1] Set to 0.0.0.0 for using DHCP or enter a static IP address
#define WIFI_GATEWAY           "192.168.1.1"     // [IpAddress2] If not using DHCP set Gateway IP address
#define WIFI_SUBNETMASK        "255.255.255.0"   // [IpAddress3] If not using DHCP set Network mask
#define WIFI_DNS               "192.168.1.1"     // [IpAddress4] If not using DHCP set DNS IP address (might be equal to WIFI_GATEWAY)

#define WIFI_CONFIG_TOOL       WIFI_RETRY        // [WifiConfig] Default tool if wifi fails to connect (default option: 4 - WIFI_RETRY)
                                                 // (WIFI_RESTART, WIFI_MANAGER, WIFI_RETRY, WIFI_WAIT, WIFI_SERIAL, WIFI_MANAGER_RESET_ONLY)
                                                 // The configuration can be changed after first setup using WifiConfig 0, 2, 4, 5, 6 and 7.

// -- Syslog --------------------------------------
#define SYS_LOG_HOST           ""                // [LogHost] (Linux) syslog host
#define SYS_LOG_PORT           514               // [LogPort] default syslog UDP port
#define SYS_LOG_LEVEL          LOG_LEVEL_NONE    // [SysLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define SERIAL_LOG_LEVEL       LOG_LEVEL_INFO    // [SerialLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define WEB_LOG_LEVEL          LOG_LEVEL_INFO    // [WebLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define MQTT_LOG_LEVEL         LOG_LEVEL_NONE    // [MqttLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)

// -- Ota -----------------------------------------
#define OTA_URL                ""  // [OtaUrl]

// -- MQTT ----------------------------------------
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
#define SUB_PREFIX             "cmnd"            // [Prefix1] Tasmota devices subscribe to %prefix%/%topic% being SUB_PREFIX/MQTT_TOPIC and SUB_PREFIX/MQTT_GRPTOPIC
#define PUB_PREFIX             "stat"            // [Prefix2] Tasmota devices publish to %prefix%/%topic% being PUB_PREFIX/MQTT_TOPIC
#define PUB_PREFIX2            "tele"            // [Prefix3] Tasmota devices publish telemetry data to %prefix%/%topic% being PUB_PREFIX2/MQTT_TOPIC/UPTIME, POWER and TIME
                                                 //   May be named the same as PUB_PREFIX
// %topic% token options (also ButtonTopic and SwitchTopic)
#define MQTT_BUTTON_TOPIC      "0"               // [ButtonTopic] MQTT button topic, "0" = same as MQTT_TOPIC, set to 'PROJECT "_BTN_%06X"' for unique topic including device MAC address
#define MQTT_SWITCH_TOPIC      "0"               // [SwitchTopic] MQTT button topic, "0" = same as MQTT_TOPIC, set to 'PROJECT "_SW_%06X"' for unique topic including device MAC address
#define MQTT_CLIENT_ID         "DVES_%06X"       // [MqttClient] Also fall back topic using Chip Id = last 6 characters of MAC address

// -- MQTT - Telemetry ----------------------------
#define TELE_PERIOD            300               // [TelePeriod] Telemetry (0 = disable, 10 - 3600 seconds)
#define TELE_ON_POWER          0                 // [SetOption59] send tele/STATE together with stat/RESULT (0 = Disable, 1 = Enable)

// -- MQTT - Domoticz -----------------------------
#define DOMOTICZ_UPDATE_TIMER  0                 // [DomoticzUpdateTimer] Send relay status (0 = disable, 1 - 3600 seconds)

// -- MQTT - Home Assistant Discovery -------------
#define HOME_ASSISTANT_DISCOVERY_ENABLE   0      // [SetOption19] Home Assistant Discovery (0 = Disable, 1 = Enable)

// -- HTTP ----------------------------------------
#define WEB_SERVER             2                 // [WebServer] Web server (0 = Off, 1 = Start as User, 2 = Start as Admin)
#define WEB_PASSWORD           ""                // [WebPassword] Web server Admin mode Password for WEB_USERNAME (empty string = Disable)
#define EMULATION              EMUL_NONE         // [Emulation] Select Belkin WeMo (single relay/light) or Hue Bridge emulation (multi relay/light) (EMUL_NONE, EMUL_WEMO or EMUL_HUE)
#define CORS_DOMAIN            ""                // [Cors] CORS Domain for preflight requests

// Dark theme
#define COLOR_TEXT                  "#eaeaea"    // [WebColor1] Global text color - Very light gray
#define COLOR_BACKGROUND            "#252525"    // [WebColor2] Global background color - Very dark gray (mostly black)
#define COLOR_FORM                  "#4f4f4f"    // [WebColor3] Form background color - Very dark gray
#define COLOR_INPUT_TEXT            "#000"       // [WebColor4] Input text color - Black
#define COLOR_INPUT                 "#ddd"       // [WebColor5] Input background color - Very light gray
#define COLOR_CONSOLE_TEXT          "#65c115"    // [WebColor6] Console text color - Strong Green
#define COLOR_CONSOLE               "#1f1f1f"    // [WebColor7] Console background color - Very dark gray (mostly black)
#define COLOR_TEXT_WARNING          "#ff5661"    // [WebColor8] Warning text color - Brick Red
#define COLOR_TEXT_SUCCESS          "#008000"    // [WebColor9] Success text color - Dark lime green
#define COLOR_BUTTON_TEXT           "#faffff"    // [WebColor10] Button text color - Very pale (mostly white) cyan
#define COLOR_BUTTON                "#1fa3ec"    // [WebColor11] Button color - Vivid blue
#define COLOR_BUTTON_HOVER          "#0e70a4"    // [WebColor12] Button color when hovered over - Dark blue
#define COLOR_BUTTON_RESET          "#d43535"    // [WebColor13] Restart/Reset/Delete button color - Strong red
#define COLOR_BUTTON_RESET_HOVER    "#931f1f"    // [WebColor14] Restart/Reset/Delete button color when hovered over - Dark red
#define COLOR_BUTTON_SAVE           "#47c266"    // [WebColor15] Save button color - Moderate lime green
#define COLOR_BUTTON_SAVE_HOVER     "#5aaf6f"    // [WebColor16] Save button color when hovered over - Dark moderate lime green
#define COLOR_TIMER_TAB_TEXT        "#faffff"    // [WebColor17] Config timer tab text color - Very pale (mostly white) cyan.
#define COLOR_TIMER_TAB_BACKGROUND  "#999"       // [WebColor18] Config timer tab background color - Dark gray
#define COLOR_TITLE_TEXT            "#eaeaea"    // [WebColor19] Title text color - Very light gray

// -- mDNS ----------------------------------------
#define MDNS_ENABLED           0                 // [SetOption55] Use mDNS (0 = Disable, 1 = Enable)

// -- Time - Up to three NTP servers in your region
//#define NTP_SERVER1            "pool.ntp.org"       // [NtpServer1] Select first NTP server by name or IP address (129.250.35.250)
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
#define APP_TIMEZONE           99                // [Timezone] +1 hour (Amsterdam) (-13 .. 14 = hours from UTC, 99 = use TIME_DST/TIME_STD)
#define APP_LEDSTATE           LED_POWER         // [LedState] Function of led
                                                 //   (LED_OFF, LED_POWER, LED_MQTTSUB, LED_POWER_MQTTSUB, LED_MQTTPUB, LED_POWER_MQTTPUB, LED_MQTT, LED_POWER_MQTT)
#define APP_LEDMASK            0xFFFF            // [LedMask] Assign Relay to Power led (0xFFFF is default)
#define APP_PULSETIME          0                 // [PulseTime] Time in 0.1 Sec to turn off power for relay 1 (0 = disabled)
//#define APP_POWERON_STATE      POWER_ALL_SAVED   // [PowerOnState] Power On Relay state
                                                 //   (POWER_ALL_OFF, POWER_ALL_ON, POWER_ALL_SAVED_TOGGLE, POWER_ALL_SAVED, POWER_ALL_ALWAYS_ON, POWER_ALL_OFF_PULSETIME_ON)
#define APP_BLINKTIME          10                // [BlinkTime] Time in 0.1 Sec to blink/toggle power for relay 1
#define APP_BLINKCOUNT         10                // [BlinkCount] Number of blinks (0 = 32000)
#define APP_SLEEP              0                 // [Sleep] Sleep time to lower energy consumption (0 = Off, 1 - 250 mSec),
#define PWM_MAX_SLEEP          10                // Sleep will be lowered to this value when light is on, to avoid flickering

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

// Section 2
#define MQTT_TELE_RETAIN     0                   // Tele messages may send retain flag (0 = off, 1 = on)

#define USE_WEBSERVER                            // Enable web server and Wifi Manager (+66k code, +8k mem)
  #define WEB_PORT             80                // Web server Port for User and Admin mode
  #define WEB_USERNAME         "admin"           // Web server Admin mode user name



#define CFG_HOLDER {cfg_holder}
#define MODULE {module}
#define MQTT_GRPTOPIC "{group_topic}"
#define MQTT_FULLTOPIC "{full_topic}"
#define MQTT_TOPIC "{topic}"
#define FRIENDLY_NAME "{f_name}"
#define STA_SSID1 "{wifi_ssid}"
#define STA_PASS1 "{wifi_pass}"
#define STA_SSID2 "{wifi_ssid_alt}"
#define STA_PASS2 "{wifi_pass_alt}"
#define MQTT_HOST "{mqtt_host}"
#define NTP_SERVER1 "{ntp}"
#define LATITUDE {latitude}
#define LONGITUDE {longitude}
#define APP_POWERON_STATE {poweron_state}
{build_flags}
#ifndef USE_ANALOG_IN
  #define USE_ADC_VCC                              // Display Vcc in Power status. Disable for use as Analog input on selected devices
#endif

#endif  // _USER_CONFIG_OVERRIDE_H_
