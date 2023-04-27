import pymem


class Menu:
    def __init__(self):
        self._pm = pymem.Pymem('EtG.exe')
        self._unity_player_module = pymem.process.module_from_name(self._pm.process_handle, 'UnityPlayer.dll').lpBaseOfDll

    def get_ptr_addr(self, base, offsets):
        try:
            addr = self._pm.read_longlong(base)
            for offset in offsets:
                if offset != offsets[-1]:
                    addr = self._pm.read_longlong(addr + offset)
            return addr + offsets[-1]
        except pymem.exception.MemoryReadError:
            return None

    def set_amount_blanks(self, value):
        address = self.get_ptr_addr(self._unity_player_module + 0x144EBB8,
                                    [0x8, 0x98, 0x28, 0x30, 0x10, 0x28, 0x568])
        if address:
            self.write(address, value)

    def set_amount_health(self, value):
        address = self.get_ptr_addr(self._unity_player_module + 0x144EBB8,
                                    [0x8, 0x98, 0x28, 0x30, 0x18, 0x50, 0x118])
        if address:
            self.write(address, value)

    def write(self, address, value):
        if isinstance(value, int):
            self._pm.write_int(address, value)
        elif isinstance(value, float):
            self._pm.write_float(address, value)
