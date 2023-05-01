import speedtest


def internet_amount_conversion(speed) -> str:
    if speed < 1000:
        speed_wit_units = str(round(speed, 3)) + " bps"
    elif speed < 1000000:
        speed_wit_units = str(round(speed / 1000, 3)) + " Kbps"
    elif speed < 1000000000:
        speed_wit_units = str(round(speed / 1000000, 3)) + " Mbps"
    else:
        speed_wit_units = str(round(speed / 1000000000, 3)) + " Gbps"

    return speed_wit_units


def get_internet_speed() -> str:
    try:
        st = speedtest.Speedtest()
        download = internet_amount_conversion(st.download())
        upload = internet_amount_conversion(st.upload())

        result = f"Download: {download}\n" \
                 f"Upload: {upload}"

        return result
    except speedtest.ConfigRetrievalError:
        return 'No internet connection'
