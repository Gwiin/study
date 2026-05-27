import logging

def main():
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logger.log",
        encoding="utf-8"
    )
    logging.debug("디버그 메시지 입니다.")
    logging.info("프로그램 시작")
    logging.warning("프로그램 종료 직전입니다.")


if __name__ == "__main__":
    main()