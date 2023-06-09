"""Hydrate configuration from local file.

Reads app config from "${PWD}/.k8scfg.json"

"""

# import json
# from pathlib import Path
# from typing import Any
# import logging
#
# from k8scfg.config import base
#
#
# FILE_NAME = ".k8scfg.json"
# SOURCE_NAME = "file"
# log = logging.getLogger(__name__)
#
#
# def read(config_path: Path) -> dict[str, Any] | None:
#     if not config_path.exists():
#         return
#
#     file = config_path / FILE_NAME
#     if not file.exists():
#         return
#
#     if content := file.read_text():
#         return json.loads(content)
#     else:
#         return
#
#
# def hydrate(data: base.Data) -> base.Data:
#     json_data = read(Path.cwd())
#     if not json_data:
#         return data
#
#     # for key in [attr for attr in dir(data) if not attr.startswith("_")]:
#     #     if value := json_data.get(key):
#     #         log.info(f"{SOURCE_NAME} FOUND: {key=} {value=}")
#     #         setattr(data, key, value)
#     #         data.sources["session_name_prefix"] = SOURCE_NAME
#
#     # --------------------------------------------------------------------------
#     for key in [attr for attr in dir(data) if not attr.startswith("_")]:
#         if key.startswith("default_"):
#             trunc_key = key.removeprefix("default_")
#             if value := json_data["default"].get(trunc_key):
#                 log.info(f"{SOURCE_NAME} FOUND: {key=} {value=}")
#                 setattr(data, trunc_key, value)
#                 data.sources[key] = SOURCE_NAME
#         elif key in ["aws_profile", "native_account", "session_name_prefix"]:
#             trunc_key = key.removeprefix("aws_")
#             if value := json_data["aws"].get(trunc_key):
#                 log.info(f"{SOURCE_NAME} FOUND: {key=} {value=}")
#                 setattr(data, trunc_key, value)
#                 data.sources[key] = SOURCE_NAME
#         # Don't use walrus operator because a "False" bool won't be captured.
#         # if value := json_data.get(key):
#         elif key in json_data:
#             value = json_data[key]
#             log.info(f"{SOURCE_NAME} FOUND: {key=} {value=}")
#             setattr(data, key, value)
#             data.sources[key] = SOURCE_NAME
#
#             if key in ["debug", "account_map"]:
#                 data.raw.seen.discard(key)
#         else:
#             log.debug(f"{SOURCE_NAME} did not find: {key=}")
#
#     # # --------------------------------------------------------------------------
#     # if "default" in json_data:
#     #     section_name = "default"
#     #     section = json_data[section_name]
#     #
#     #     # data.default_account = section.get("account") or data.default_account
#     #     short_key = "account"
#     #     if value := section.get(short_key):
#     #         key = f"{section_name}_{short_key}"
#     #         log.info(f"{SOURCE_NAME} FOUND: {key=} {value=}")
#     #         setattr(data, key, value)
#     #         data.sources[key] = SOURCE_NAME
#     #
#     #     data.default_region = section.get("region") or data.default_region
#     #
#     #     data.default_namespace = section.get("namespace") or data.default_namespace
#
#     # # --------------------------------------------------------------------------
#     # if "aws" in json_data:
#     #     section = json_data["aws"]
#     #     data.aws_profile = section.get("profile") or data.aws_profile
#     #     data.native_account = section.get("native_account") or data.native_account
#     #     data.session_name_prefix = section.get("session_name_prefix") or data.session_name_prefix
#     #
#     # # --------------------------------------------------------------------------
#     # data.debug = json_data.get("debug") or data.debug
#     # data.account_map = json_data.get("account_map") or data.account_map
#
#     #
#     #
#     #
#
#     # # --------------------------------------------------------------------------
#     # if "default" in json_data:
#     #     section = json_data["default"]
#     #     data.default_account = section.get("account") or data.default_account
#     #     data.default_region = section.get("region") or data.default_region
#     #     data.default_namespace = section.get("namespace") or data.default_namespace
#     #
#     # # --------------------------------------------------------------------------
#     # if "aws" in json_data:
#     #     section = json_data["aws"]
#     #     data.aws_profile = section.get("profile") or data.aws_profile
#     #     data.native_account = section.get("native_account") or data.native_account
#     #     data.session_name_prefix = section.get("session_name_prefix") or data.session_name_prefix
#     #
#     # # --------------------------------------------------------------------------
#     # data.debug = json_data.get("debug") or data.debug
#     # data.account_map = json_data.get("account_map") or data.account_map
#
#     return data
