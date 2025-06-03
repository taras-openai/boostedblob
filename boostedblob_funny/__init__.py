from __future__ import annotations

from boostedblob.path import CloudPath
import urllib
from dataclasses import dataclass
from typing import AsyncIterator, Optional

from boostedblob.listing import list_blobs
from boostedblob.listing import DirEntry

@dataclass(frozen=True)
class MyFunnyPath(CloudPath):
    url: str

    @staticmethod
    def is_cloud_path(url: urllib.parse.ParseResult) -> bool:
        return url.scheme == "myfunny"

    @staticmethod
    def from_str(url: str) -> MyFunnyPath:
        return MyFunnyPath(url)


    def ensure_directory_like(self) -> MyFunnyPath:
        return self



@list_blobs.register  # type: ignore
async def _myfunny_listblobs(path: MyFunnyPath, delimiter: Optional[str], allow_prefix: bool = False) -> AsyncIterator[DirEntry]:
    child1 = MyFunnyPath(path.url + '/ma')
    yield DirEntry(path=child1, is_dir=False, is_file=True, stat=None)
    child2 = MyFunnyPath(path.url + '/cool')
    yield DirEntry(path=child2, is_dir=False, is_file=True, stat=None)




ExportedCloudPath = MyFunnyPath

__all__ = ["ExportedCloudPath"]
