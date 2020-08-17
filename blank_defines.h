//generate undefines:
//grep "#define" ../Tasmota/tasmota/my_user_config.h | grep -v _MY_USER_CONFIG_H_ | sed 's/[\/ ]*#define \([A-Za-z_0-9]*\).*/#undef \1/' | sort | uniq | tee -a blank_defines.h
//Config for {name} generated on {datetime}
#ifndef _USER_CONFIG_OVERRIDE_H_
#define _USER_CONFIG_OVERRIDE_H_

/*********************************************************************************************\
 * SECTION 0
 * - Undefine everything first
\*********************************************************************************************/

#undef APP_BLINKCOUNT
#undef APP_BLINKTIME
#undef APP_DISABLE_POWERCYCLE
#undef APP_ENABLE_LEDLINK
#undef APP_FLASH_CYCLE
#undef APP_INTERLOCK_GROUP_1
#undef APP_INTERLOCK_GROUP_2
#undef APP_INTERLOCK_GROUP_3
#undef APP_INTERLOCK_GROUP_4
#undef APP_INTERLOCK_MODE
#undef APP_LEDMASK
#undef APP_LEDSTATE
#undef APP_NORMAL_SLEEP
#undef APP_NO_RELAY_SCAN
#undef APP_POWERON_STATE
#undef APP_PULSETIME
#undef APP_SLEEP
#undef APP_TIMEZONE
#undef BOOT_LOOP_OFFSET
#undef BUZZER_ENABLE
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
#undef COUNTER_RESET
#undef DDS2382_SPEED
#undef DDSU666_SPEED
#undef DEBUG_TASMOTA_CORE
#undef DEBUG_TASMOTA_DRIVER
#undef DEBUG_TASMOTA_SENSOR
#undef DEEPSLEEP_BOOTCOUNT
#undef DEEPSLEEP_LWT_HA_DISCOVERY
#undef DEVICE_GROUPS_ADDRESS
#undef DEVICE_GROUPS_PORT
#undef DOMOTICZ_IN_TOPIC
#undef DOMOTICZ_OUT_TOPIC
#undef DOMOTICZ_UPDATE_TIMER
#undef DS18X20_PULL_UP
#undef EMULATION
#undef ENERGY_DDS2382_MODE
#undef ENERGY_HARDWARE_TOTALS
#undef ENERGY_RESOLUTION
#undef ENERGY_VOLTAGE_ALWAYS
#undef ETH_ADDR
#undef ETH_CLKMODE
#undef ETH_TYPE
#undef EXS_MCU_CMNDS
#undef FALLBACK_MODULE
#undef FIRMWARE_DISPLAYS
#undef FIRMWARE_IR
#undef FIRMWARE_IR_CUSTOM
#undef FIRMWARE_KNX_NO_EMULATION
#undef FIRMWARE_LITE
#undef FIRMWARE_MINIMAL
#undef FIRMWARE_SENSORS
#undef FRIENDLY_NAME
#undef GUI_SHOW_HOSTNAME
#undef HASS_AS_LIGHT
#undef HOME_ASSISTANT_DISCOVERY_ENABLE
#undef HOME_ASSISTANT_DISCOVERY_PREFIX
#undef HUMIDITY_RESOLUTION
#undef IEM3000_ADDR
#undef IEM3000_SPEED
#undef IR_ADD_RAW_DATA
#undef IR_DATA_RADIX
#undef IR_RCV_BUFFER_SIZE
#undef IR_RCV_MIN_UNKNOWN_SIZE
#undef IR_RCV_TIMEOUT
#undef KEY_DEBOUNCE_TIME
#undef KEY_DISABLE_MULTIPRESS
#undef KEY_HOLD_TIME
#undef KEY_ONLY_SINGLE_PRESS
#undef KEY_SWAP_DOUBLE_PRESS
#undef KNX_ENABLED
#undef KNX_ENHANCED
#undef LATITUDE
#undef LE01MR_ADDR
#undef LE01MR_SPEED
#undef LIGHT_ALEXA_CT_RANGE
#undef LIGHT_CHANNEL_MODE
#undef LIGHT_CLOCK_DIRECTION
#undef LIGHT_COLOR_RADIX
#undef LIGHT_MODE
#undef LIGHT_PAIRS_CO2
#undef LIGHT_POWER_CONTROL
#undef LIGHT_PWM_CT_MODE
#undef LIGHT_SLIDER_POWER
#undef LONGITUDE
#undef MAX31865_PTD_BIAS
#undef MAX31865_PTD_RES
#undef MAX31865_PTD_WIRES
#undef MAX31865_REF_RES
#undef MDNS_ENABLED
#undef MGS_SENSOR_ADDR
#undef MODULE
#undef MP3_VOLUME
#undef MQTT_APPEND_TIMEZONE
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
#undef MQTT_GROUPTOPIC_FORMAT
#undef MQTT_GRPTOPIC
#undef MQTT_HOST
#undef MQTT_HOST_DISCOVERY
#undef MQTT_INDEX_SEPARATOR
#undef MQTT_LOG_LEVEL
#undef MQTT_LWT_MESSAGE
#undef MQTT_NO_HOLD_RETAIN
#undef MQTT_NO_RETAIN
#undef MQTT_PASS
#undef MQTT_PORT
#undef MQTT_POWER_FORMAT
#undef MQTT_POWER_RETAIN
#undef MQTT_RESULT_COMMAND
#undef MQTT_SENSOR_RETAIN
#undef MQTT_STATUS_OFF
#undef MQTT_STATUS_ON
#undef MQTT_SWITCH_RETAIN
#undef MQTT_SWITCH_TOPIC
#undef MQTT_TELE_RETAIN
#undef MQTT_TOPIC
#undef MQTT_TUYA_RECEIVED
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
#undef OTA_COMPATIBILITY
#undef OTA_URL
#undef PCF8574_INVERT_PORTS
#undef PMS_MODEL_PMS3003
#undef PRESSURE_CONVERSION
#undef PRESSURE_RESOLUTION
#undef PROJECT
#undef PUB_PREFIX
#undef PUB_PREFIX2
#undef PWM_MAX_SLEEP
#undef RF_DATA_RADIX
#undef ROTARY_MAX_STEPS
#undef ROTARY_V1
#undef SAVE_DATA
#undef SAVE_STATE
#undef SDM120_SPEED
#undef SDM630_SPEED
#undef SERIAL_LOG_LEVEL
#undef SEVENSEG_ADDRESS1
#undef SHUTTER_SUPPORT
#undef SOLAXX1_PV2
#undef SOLAXX1_SPEED
#undef STARTING_OFFSET
#undef STA_PASS1
#undef STA_PASS2
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
#undef THERMOSTAT_CONTROLLER_OUTPUTS
#undef THERMOSTAT_DUTYCYCLE_AUTOTUNE
#undef THERMOSTAT_PEAKNUMBER_AUTOTUNE
#undef THERMOSTAT_PROP_BAND
#undef THERMOSTAT_RELAY_NUMBER
#undef THERMOSTAT_SENSOR_NAME
#undef THERMOSTAT_SWITCH_NUMBER
#undef THERMOSTAT_TEMP_BAND_NO_PEAK_DET
#undef THERMOSTAT_TEMP_FROST_PROTECT
#undef THERMOSTAT_TEMP_HYSTERESIS
#undef THERMOSTAT_TEMP_INIT
#undef THERMOSTAT_TEMP_PI_RAMPUP_ACC_E
#undef THERMOSTAT_TEMP_RAMPUP_DELTA_IN
#undef THERMOSTAT_TEMP_RAMPUP_DELTA_OUT
#undef THERMOSTAT_TEMP_RESET_ANTI_WINDUP
#undef THERMOSTAT_TEMP_SENS_NUMBER
#undef THERMOSTAT_TIME_ALLOW_RAMPUP
#undef THERMOSTAT_TIME_MANUAL_TO_AUTO
#undef THERMOSTAT_TIME_MAX_ACTION
#undef THERMOSTAT_TIME_MAX_AUTOTUNE
#undef THERMOSTAT_TIME_MAX_OUTPUT_INCONSIST
#undef THERMOSTAT_TIME_MIN_ACTION
#undef THERMOSTAT_TIME_MIN_TURNOFF_ACTION
#undef THERMOSTAT_TIME_OUTPUT_DELAY
#undef THERMOSTAT_TIME_PI_CYCLE
#undef THERMOSTAT_TIME_RAMPUP_CYCLE
#undef THERMOSTAT_TIME_RAMPUP_MAX
#undef THERMOSTAT_TIME_RESET
#undef THERMOSTAT_TIME_SENS_LOST
#undef THERMOSTAT_TIME_STD_DEV_PEAK_DET_OK
#undef TIMERS_ENABLED
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
#undef TUYA_SETOPTION_20
#undef USER_TEMPLATE
#undef USE_4K_RSA
#undef USE_A4988_STEPPER
#undef USE_ADC_VCC
#undef USE_ADE7953
#undef USE_ADS1115
#undef USE_AHT1x
#undef USE_ALECTO_V2
#undef USE_APDS9960
#undef USE_APDS9960_COLOR
#undef USE_APDS9960_GESTURE
#undef USE_APDS9960_PROXIMITY
#undef USE_APDS9960_STARTMODE
#undef USE_ARDUINO_OTA
#undef USE_ARILUX_RF
#undef USE_ARMTRONIX_DIMMERS
#undef USE_AS3935
#undef USE_AZ7798
#undef USE_BH1750
#undef USE_BL0940
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
#undef USE_DEVICE_GROUPS
#undef USE_DEVICE_GROUPS_SEND
#undef USE_DGR_LIGHT_SEQUENCE
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
#undef USE_DISPLAY_SEVENSEG
#undef USE_DISPLAY_SH1106
#undef USE_DISPLAY_SSD1306
#undef USE_DISPLAY_SSD1351
#undef USE_DOMOTICZ
#undef USE_DS1624
#undef USE_DS18x20
#undef USE_DS3231
#undef USE_ELECTRIQ_MOODL
#undef USE_EMULATION_HUE
#undef USE_EMULATION_WEMO
#undef USE_ENERGY_MARGIN_DETECTION
#undef USE_ENERGY_POWER_LIMIT
#undef USE_ETHERNET
#undef USE_EXPRESSION
#undef USE_EXS_DIMMER
#undef USE_FLOG
#undef USE_GPS
#undef USE_HDC1080
#undef USE_HIH6
#undef USE_HM10
#undef USE_HOME_ASSISTANT
#undef USE_HOTPLUG
#undef USE_HP303B
#undef USE_HPMA
#undef USE_HRE
#undef USE_HRXL
#undef USE_HTU
#undef USE_HX711
#undef USE_HX711_GUI
#undef USE_I2C
#undef USE_IAQ
#undef USE_IBEACON
#undef USE_IEM3000
#undef USE_INA219
#undef USE_INA226
#undef USE_IR_RECEIVE
#undef USE_IR_REMOTE
#undef USE_IR_SEND_NEC
#undef USE_IR_SEND_RC5
#undef USE_IR_SEND_RC6
#undef USE_JAVASCRIPT_ES6
#undef USE_KEELOQ
#undef USE_KNX
#undef USE_KNX_WEB_MENU
#undef USE_LE01MR
#undef USE_LIGHT_PALETTE
#undef USE_LM75AD
#undef USE_LMT01
#undef USE_MAX31855
#undef USE_MAX31865
#undef USE_MAX44009
#undef USE_MCP230xx
#undef USE_MCP230xx_ADDR
#undef USE_MCP230xx_DISPLAYOUTPUT
#undef USE_MCP230xx_OUTPUT
#undef USE_MCP39F501
#undef USE_MCP9808
#undef USE_MGC3130
#undef USE_MGS
#undef USE_MHZ19
#undef USE_MIBLE
#undef USE_MI_ESP32
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
#undef USE_NRF24
#undef USE_OPENTHERM
#undef USE_PAJ7620
#undef USE_PCA9685
#undef USE_PCA9685_ADDR
#undef USE_PCA9685_FREQ
#undef USE_PCF8574
#undef USE_PING
#undef USE_PMS5003
#undef USE_PN532_CAUSE_EVENTS
#undef USE_PN532_DATA_FUNCTION
#undef USE_PN532_DATA_RAW
#undef USE_PN532_HSU
#undef USE_PROMETHEUS
#undef USE_PS_16_DZ
#undef USE_PWM_DIMMER
#undef USE_PWM_DIMMER_REMOTE
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
#undef USE_SONOFF_D1
#undef USE_SONOFF_IFAN
#undef USE_SONOFF_L1
#undef USE_SONOFF_RF
#undef USE_SONOFF_SC
#undef USE_SPI
#undef USE_SPS30
#undef USE_SR04
#undef USE_SUNRISE
#undef USE_TASMOTA_CLIENT
#undef USE_TASMOTA_CLIENT_FLASH_SPEED
#undef USE_TASMOTA_CLIENT_SERIAL_SPEED
#undef USE_TCP_BRIDGE
#undef USE_TELEGRAM
#undef USE_TELEGRAM_FINGERPRINT
#undef USE_TELEINFO
#undef USE_TELEINFO_STANDARD
#undef USE_THEO_V2
#undef USE_THERMOSTAT
#undef USE_TIMERS
#undef USE_TIMERS_WEB
#undef USE_TLS
#undef USE_TM1638
#undef USE_TSL2561
#undef USE_TSL2591
#undef USE_TUYA_MCU
#undef USE_TUYA_TIME
#undef USE_TX20_WIND_SENSOR
#undef USE_TX23_WIND_SENSOR
#undef USE_UNISHOX_COMPRESSION
#undef USE_VEML6070
#undef USE_VEML6070_RSET
#undef USE_VEML6070_SHOW_RAW
#undef USE_VEML6075
#undef USE_VEML7700
#undef USE_VL53L0X
#undef USE_WEBCAM
#undef USE_WEBSEND_RESPONSE
#undef USE_WEBSERVER
#undef USE_WEMOS_MOTOR_V1
#undef USE_WINDMETER
#undef USE_WS2812
#undef USE_WS2812_CTYPE
#undef USE_WS2812_DMA
#undef USE_WS2812_HARDWARE
#undef USE_ZIGBEE
#undef USE_ZIGBEE_CHANNEL
#undef USE_ZIGBEE_COALESCE_ATTR_TIMER
#undef USE_ZIGBEE_EZSP
#undef USE_ZIGBEE_MANUFACTURER
#undef USE_ZIGBEE_MODELID
#undef USE_ZIGBEE_TXRADIO_DBM
#undef USE_ZIGBEE_ZNP
#undef W1_PARASITE_POWER
#undef WEBSERVER_ADVERTISE
#undef WEB_LOG_LEVEL
#undef WEB_PASSWORD
#undef WEB_PORT
#undef WEB_SERVER
#undef WEB_USERNAME
#undef WEMOS_MOTOR_V1_ADDR
#undef WEMOS_MOTOR_V1_FREQ
#undef WIFI_AP_PASSPHRASE
#undef WIFI_ARP_INTERVAL
#undef WIFI_CONFIG_TOOL
#undef WIFI_DNS
#undef WIFI_GATEWAY
#undef WIFI_IP_ADDRESS
#undef WIFI_SCAN_AT_RESTART
#undef WIFI_SCAN_REGULARLY
#undef WIFI_SOFT_AP_CHANNEL
#undef WIFI_SUBNETMASK
#undef WS2812_LEDS
#undef ZIGBEE_FRIENDLY_NAMES

// force the compiler to show a warning to confirm that this file is inlcuded
#warning "**** user_config_override.h: Using Settings from this File ****"

/*********************************************************************************************\
 * SECTION 1
 * - After initial load any change here only take effect if CFG_HOLDER is changed too
\*********************************************************************************************/

// -- Project -------------------------------------
#define PROJECT                "tasmota"         // PROJECT is used as the default topic delimiter

// If not selected the default will be SONOFF_BASIC
//#define MODULE                 SONOFF_BASIC      // [Module] Select default module from tasmota_template.h
#ifdef ESP8266
#define FALLBACK_MODULE        SONOFF_BASIC      // [Module2] Select default module on fast reboot where USER_MODULE is user template
#else // ESP32
#define FALLBACK_MODULE        WEMOS             // [Module2] Select default module on fast reboot where USER_MODULE is user template
#endif

#define SAVE_DATA              1                 // [SaveData] Save changed parameters to Flash (0 = disable, 1 - 3600 seconds)
#define SAVE_STATE             false             // [SetOption0] Save changed power state to Flash (false = disable, true = enable)
#define BOOT_LOOP_OFFSET       1                 // [SetOption36] Number of boot loops before starting restoring defaults (0 = disable, 1..200 = boot loops offset)

// -- Wifi ----------------------------------------
#define WIFI_IP_ADDRESS        "0.0.0.0"         // [IpAddress1] Set to 0.0.0.0 for using DHCP or enter a static IP address
#define WIFI_GATEWAY           ""     // [IpAddress2] If not using DHCP set Gateway IP address
#define WIFI_SUBNETMASK        ""   // [IpAddress3] If not using DHCP set Network mask
#define WIFI_DNS               ""     // [IpAddress4] If not using DHCP set DNS IP address (might be equal to WIFI_GATEWAY)

#define WIFI_AP_PASSPHRASE     ""                // AccessPoint passphrase. For WPA2 min 8 char, for open use "" (max 63 char).
#define WIFI_CONFIG_TOOL       WIFI_RETRY        // [WifiConfig] Default tool if wifi fails to connect (default option: 4 - WIFI_RETRY)
                                                 // (WIFI_RESTART, WIFI_MANAGER, WIFI_RETRY, WIFI_WAIT, WIFI_SERIAL, WIFI_MANAGER_RESET_ONLY)
                                                 // The configuration can be changed after first setup using WifiConfig 0, 2, 4, 5, 6 and 7.

#define WIFI_ARP_INTERVAL      0                 // [SetOption41] Send gratuitous ARP interval
#define WIFI_SCAN_AT_RESTART   true              // [SetOption56] Scan wifi network at restart for configured AP's
#define WIFI_SCAN_REGULARLY    true              // [SetOption57] Scan wifi network every 44 minutes for configured AP's

// -- Syslog --------------------------------------
#define SYS_LOG_HOST           ""                // [LogHost] (Linux) syslog host
#define SYS_LOG_PORT           514               // [LogPort] default syslog UDP port
#define SYS_LOG_LEVEL          LOG_LEVEL_NONE    // [SysLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define SERIAL_LOG_LEVEL       LOG_LEVEL_INFO    // [SerialLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define WEB_LOG_LEVEL          LOG_LEVEL_INFO    // [WebLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)
#define MQTT_LOG_LEVEL         LOG_LEVEL_NONE    // [MqttLog] (LOG_LEVEL_NONE, LOG_LEVEL_ERROR, LOG_LEVEL_INFO, LOG_LEVEL_DEBUG, LOG_LEVEL_DEBUG_MORE)

// -- Ota -----------------------------------------
#define OTA_URL                ""  // [OtaUrl]
#define OTA_COMPATIBILITY      false             // [SetOption78] Disable OTA compatibility check

// -- MQTT ----------------------------------------
#define MQTT_USE               true              // [SetOption3] Select default MQTT use (false = Off, true = On)

#define MQTT_FINGERPRINT1      "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"  // [MqttFingerprint1] (auto-learn)
#define MQTT_FINGERPRINT2      "DA 39 A3 EE 5E 6B 4B 0D 32 55 BF EF 95 60 18 90 AF D8 07 09"  // [MqttFingerprint2] (invalid)
#define MQTT_PORT              1883              // [MqttPort] MQTT port (10123 on CloudMQTT)
#define MQTT_USER              "DVES_USER"       // [MqttUser] MQTT user
#define MQTT_PASS              "DVES_PASS"       // [MqttPassword] MQTT password

#define MQTT_BUTTON_RETAIN     false             // [ButtonRetain] Button may send retain flag (false = off, true = on)
#define MQTT_POWER_RETAIN      false             // [PowerRetain] Power status message may send retain flag (false = off, true = on)
#define MQTT_SWITCH_RETAIN     false             // [SwitchRetain] Switch may send retain flag (false = off, true = on)
#define MQTT_SENSOR_RETAIN     false             // [SensorRetain] Sensor may send retain flag (false = off, true = on)
#define MQTT_NO_HOLD_RETAIN    false             // [SetOption62] Disable retain flag on HOLD messages
//#define MQTT_NO_RETAIN                         // Disable all retain flags (This don't include LWT!) if unsupported by broker (eg Losant)

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
#define MQTT_GROUPTOPIC_FORMAT false             // [SetOption75] GroupTopic replaces %topic% (false) or fixed topic cmnd/grouptopic (true)
#define MQTT_BUTTON_TOPIC      "0"               // [ButtonTopic] MQTT button topic, "0" = same as MQTT_TOPIC, set to 'PROJECT "_BTN_%06X"' for unique topic including device MAC address
#define MQTT_SWITCH_TOPIC      "0"               // [SwitchTopic] MQTT button topic, "0" = same as MQTT_TOPIC, set to 'PROJECT "_SW_%06X"' for unique topic including device MAC address
#define MQTT_CLIENT_ID         "DVES_%06X"       // [MqttClient] Also fall back topic using last 6 characters of MAC address or use "DVES_%12X" for complete MAC address

// -- MQTT - Telemetry ----------------------------
#define TELE_PERIOD            300               // [TelePeriod] Telemetry (0 = disable, 10 - 3600 seconds)
#define TELE_ON_POWER          false             // [SetOption59] send tele/STATE together with stat/RESULT (false = Disable, true = Enable)

// -- MQTT - Domoticz -----------------------------
#define DOMOTICZ_UPDATE_TIMER  0                 // [DomoticzUpdateTimer] Send relay status (0 = disable, 1 - 3600 seconds)

// -- MQTT - Home Assistant Discovery -------------
#define HOME_ASSISTANT_DISCOVERY_ENABLE   false  // [SetOption19] Home Assistant Discovery (false = Disable, true = Enable)
#define HASS_AS_LIGHT          false             // [SetOption30] Enforce HAss autodiscovery as light
//#define DEEPSLEEP_LWT_HA_DISCOVERY             // Enable LWT topic and its payloads for read-only sensors (Status sensor not included) and binary_sensors on HAss Discovery (Commented out: all read-only sensors and binary_sensors
                                                 // won't be shown as OFFLINE on Home Assistant when the device is DeepSleeping - NOTE: This is only for read-only sensors and binary_sensors, relays will be shown as OFFLINE)

// -- MQTT - Options ------------------------------
#define MQTT_RESULT_COMMAND    false             // [SetOption4]  Switch between MQTT RESULT or COMMAND
#define MQTT_LWT_MESSAGE       false             // [SetOption10] Switch between MQTT LWT OFFLINE or empty message
#define MQTT_POWER_FORMAT      false             // [SetOption26] Switch between POWER or POWER1 for single power devices
#define MQTT_APPEND_TIMEZONE   false             // [SetOption52] Append timezone to JSON time
#define MQTT_BUTTON_SWITCH_FORCE_LOCAL   false   // [SetOption61] Force local operation when button/switch topic is set (false = off, true = on)
#define MQTT_INDEX_SEPARATOR   false             // [SetOption64] Enable "_" instead of "-" as sensor index separator
#define MQTT_TUYA_RECEIVED     false             // [SetOption66] Enable TuyaMcuReceived messages over Mqtt

// -- HTTP ----------------------------------------
#define WEB_SERVER             2                 // [WebServer] Web server (0 = Off, 1 = Start as User, 2 = Start as Admin)
#define WEB_PASSWORD           ""                // [WebPassword] Web server Admin mode Password for WEB_USERNAME (empty string = Disable)
#define EMULATION              EMUL_NONE         // [Emulation] Select Belkin WeMo (single relay/light) or Hue Bridge emulation (multi relay/light) (EMUL_NONE, EMUL_WEMO or EMUL_HUE)
#define CORS_DOMAIN            ""                // [Cors] CORS Domain for preflight requests

// -- HTTP Options --------------------------------
#define GUI_SHOW_HOSTNAME      false             // [SetOption53] Show hostname and IP address in GUI main menu

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

// -- KNX -----------------------------------------
#define KNX_ENABLED            false             // [Knx_Enabled] Enable KNX protocol
#define KNX_ENHANCED           false             // [Knx_Enhanced] Enable KNX Enhanced Mode

// -- mDNS ----------------------------------------
#define MDNS_ENABLED           false             // [SetOption55] Use mDNS (false = Disable, true = Enable)

// -- Time - Up to three NTP servers in your region
// #define NTP_SERVER1            "pool.ntp.org"       // [NtpServer1] Select first NTP server by name or IP address (129.250.35.250)
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
#define APP_LEDMASK            0xFFFF            // [LedMask] Assign Relay to Power led (0xFFFF is default)
#define APP_ENABLE_LEDLINK     false             // [SetOption31] Enable link led blinking

#define APP_PULSETIME          0                 // [PulseTime] Time in 0.1 Sec to turn off power for relay 1 (0 = disabled)
// #define APP_POWERON_STATE      POWER_ALL_SAVED   // [PowerOnState] Power On Relay state
                                                 //   (POWER_ALL_OFF, POWER_ALL_ON, POWER_ALL_SAVED_TOGGLE, POWER_ALL_SAVED, POWER_ALL_ALWAYS_ON, POWER_ALL_OFF_PULSETIME_ON)
#define APP_BLINKTIME          10                // [BlinkTime] Time in 0.1 Sec to blink/toggle power for relay 1
#define APP_BLINKCOUNT         10                // [BlinkCount] Number of blinks (0 = 32000)

#define APP_NORMAL_SLEEP       false             // [SetOption60] Enable normal sleep instead of dynamic sleep
#define APP_SLEEP              0                 // [Sleep] Sleep time to lower energy consumption (0 = Off, 1 - 250 mSec),
#define PWM_MAX_SLEEP          10                // Sleep will be lowered to this value when light is on, to avoid flickering

#define KEY_DEBOUNCE_TIME      50                // [ButtonDebounce] Number of mSeconds button press debounce time
#define KEY_HOLD_TIME          40                // [SetOption32] Number of 0.1 seconds to hold Button or external Pushbutton before sending HOLD message
#define KEY_DISABLE_MULTIPRESS false             // [SetOption1]  Disable button multipress
#define KEY_SWAP_DOUBLE_PRESS  false             // [SetOption11] Swap button single and double press functionality
#define KEY_ONLY_SINGLE_PRESS  false             // [SetOption13] Enable only single press to speed up button press recognition

#define SWITCH_DEBOUNCE_TIME   50                // [SwitchDebounce] Number of mSeconds switch press debounce time
#define SWITCH_MODE            TOGGLE            // [SwitchMode] TOGGLE, FOLLOW, FOLLOW_INV, PUSHBUTTON, PUSHBUTTON_INV, PUSHBUTTONHOLD, PUSHBUTTONHOLD_INV, PUSHBUTTON_TOGGLE, TOGGLEMULTI, FOLLOWMULTI, FOLLOWMULTI_INV (the wall switch state)

#define TEMP_CONVERSION        false             // [SetOption8] Return temperature in (false = Celsius or true = Fahrenheit)
#define PRESSURE_CONVERSION    false             // [SetOption24] Return pressure in (false = hPa or true = mmHg)
#define TEMP_RESOLUTION        1                 // [TempRes] Maximum number of decimals (0 - 3) showing sensor Temperature
#define HUMIDITY_RESOLUTION    1                 // [HumRes] Maximum number of decimals (0 - 3) showing sensor Humidity
#define PRESSURE_RESOLUTION    1                 // [PressRes] Maximum number of decimals (0 - 3) showing sensor Pressure
#define ENERGY_RESOLUTION      3                 // [EnergyRes] Maximum number of decimals (0 - 5) showing energy usage in kWh
#define CALC_RESOLUTION        3                 // [CalcRes] Maximum number of decimals (0 - 7) used in commands ADD, SUB, MULT and SCALE

#define APP_FLASH_CYCLE        false             // [SetOption12] Switch between dynamic or fixed slot flash save location
#define APP_NO_RELAY_SCAN      false             // [SetOption63] Don't scan relay power state at restart
#define APP_DISABLE_POWERCYCLE false             // [SetOption65] Disable fast power cycle detection for device reset
#define DEEPSLEEP_BOOTCOUNT    false             // [SetOption76] Enable incrementing bootcount when deepsleep is enabled

#define APP_INTERLOCK_MODE     false             // [Interlock] Relay interlock mode
#define APP_INTERLOCK_GROUP_1  0xFF              // [Interlock] Relay bitmask for interlock group 1 (0xFF if undef)
//#define APP_INTERLOCK_GROUP_2  0x00              // [Interlock] Relay bitmask for interlock group 2 (0x00 if undef)
//#define APP_INTERLOCK_GROUP_3  0x00              // [Interlock] Relay bitmask for interlock group 3 (0x00 if undef)
//#define APP_INTERLOCK_GROUP_4  0x00              // [Interlock] Relay bitmask for interlock group 4 (0x00 if undef)

// -- Lights --------------------------------------
#define WS2812_LEDS            30                // [Pixels] Number of WS2812 LEDs to start with (max is 512)
#define LIGHT_MODE             true              // [SetOption15] Switch between commands PWM or COLOR/DIMMER/CT/CHANNEL
#define LIGHT_CLOCK_DIRECTION  false             // [SetOption16] Switch WS2812 clock between clockwise or counter-clockwise
#define LIGHT_COLOR_RADIX      false             // [SetOption17] Switch between decimal or hexadecimal color output (false = hexadecimal, true = decimal)
#define LIGHT_PAIRS_CO2        false             // [SetOption18] Enable Pair light signal with CO2 sensor
#define LIGHT_POWER_CONTROL    false             // [SetOption20] Enable power control in relation to Dimmer/Color/Ct changes
#define LIGHT_CHANNEL_MODE     false             // [SetOption68] Enable multi-channels PWM instead of Color PWM
#define LIGHT_SLIDER_POWER     false             // [SetOption77] Do not power off if slider moved to far left
#define LIGHT_ALEXA_CT_RANGE   false             // [SetOption82] Reduced CT range for Alexa
#define LIGHT_PWM_CT_MODE      false             // [SetOption92] Set PWM Mode from regular PWM to ColorTemp control (Xiaomi Philips ...) a.k.a. module 48 mode

// -- Energy --------------------------------------
#define ENERGY_VOLTAGE_ALWAYS  false             // [SetOption21] Enable show voltage even if powered off
#define ENERGY_DDS2382_MODE    false             // [SetOption71] Enable DDS2382 different Modbus registers for Active Energy (#6531)
#define ENERGY_HARDWARE_TOTALS false             // [SetOption72] Enable hardware energy total counter as reference (#6561)

// -- Other Options -------------------------------
#define TIMERS_ENABLED         false             // [Timers] Enable Timers
#define RF_DATA_RADIX          false             // [SetOption28] RF receive data format (false = hexadecimal, true = decimal)
#define IR_DATA_RADIX          false             // [SetOption29] IR receive data format (false = hexadecimal, true = decimal)
#define TUYA_SETOPTION_20      false             // [SetOption54] Apply SetOption20 settings to Tuya device
#define IR_ADD_RAW_DATA        false             // [SetOption58] Add IR Raw data to JSON message
#define BUZZER_ENABLE          false             // [SetOption67] Enable buzzer when available
#define DS18X20_PULL_UP        false             // [SetOption74] Enable internal pullup for single DS18x20 sensor
#define COUNTER_RESET          false             // [SetOption79] Enable resetting of counters after telemetry was sent
#define SHUTTER_SUPPORT        false             // [SetOption80] Enable shutter support
#define PCF8574_INVERT_PORTS   false             // [SetOption81] Invert all ports on PCF8574 devices
#define ZIGBEE_FRIENDLY_NAMES  false             // [SetOption83] Enable Zigbee FriendlyNames instead of ShortAddresses when possible

/*********************************************************************************************\
 * END OF SECTION 1
 *
 * SECTION 2
 * - Enable a feature by removing both // in front of it
 * - Disable a feature by preceding it with //
\*********************************************************************************************/

// -- MQTT ----------------------------------------
#define MQTT_TELE_RETAIN     0                   // Tele messages may send retain flag (0 = off, 1 = on)
#define MQTT_CLEAN_SESSION   1                   // Mqtt clean session connection (0 = No clean session, 1 = Clean session (default))

// -- HTTP ----------------------------------------
#define USE_WEBSERVER                            // Enable web server and Wifi Manager (+66k code, +8k mem)
  #define WEB_PORT             80                // Web server Port for User and Admin mode
  #define WEB_USERNAME         "admin"           // Web server Admin mode user name

// -- Compression ---------------------------------
#define USE_UNISHOX_COMPRESSION                  // Add support for string compression in Rules or Scripts

// -- Rules or Script  ----------------------------
// Select none or only one of the below defines USE_RULES or USE_SCRIPT
#define USE_RULES                                // Add support for rules (+8k code)
  #define USE_RULES_COMPRESSION                  // Compresses rules in Flash at about ~50% (+3.3k code)
//#define USE_SCRIPT                               // Add support for script (+17k code)
  //#define USE_SCRIPT_FATFS 4                     // Script: Add FAT FileSystem Support

 #define USE_EXPRESSION                         // Add support for expression evaluation in rules (+3k2 code, +64 bytes mem)
   #define SUPPORT_IF_STATEMENT                 // Add support for IF statement in rules (+4k2 code, -332 bytes mem)
 #define SUPPORT_MQTT_EVENT                     // Support trigger event with MQTT subscriptions (+3k5 code)

/*********************************************************************************************\
 * SECTION 3
 * - Template to be filled in per device
\*********************************************************************************************/

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
{tasmota_defines}
#ifndef USE_ANALOG_IN
  #define USE_ADC_VCC                              // Display Vcc in Power status. Disable for use as Analog input on selected devices
#endif

#endif  // _USER_CONFIG_OVERRIDE_H_