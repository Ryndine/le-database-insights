import os
import re

# First setup 
class fixer:
    src_path = '8.4_itemdb.js'
    fixed_path = '8.4_itemdb_fixed.json'

    @staticmethod
    def fix() -> None:
        if os.path.exists(fixer.fixed_path):
            os.remove(fixer.fixed_path)
        def prefix_and_suffix_fixes() -> str:
            prefix = re.compile(r'window.itemDB=')
            endpoint = re.compile(r'};.*?$')
            with open(fixer.src_path, 'r') as s:
                file = s.read()
                start = prefix.search(file).span()[1] 
                end = endpoint.search(file).span()[0] + 1

            text = file[start:end]
            return text

        def replace_fixes(res: str) -> str:
            def replace_keys(matchobj):
                return f'"{matchobj.group(0)}"'

            def replace_decimals(matchobj):
                return f'0{matchobj.group(0)}'\

            def replace_bools(matchobj):
                if matchobj.group(0) == '!0':
                    return 'true'
                else:
                    return 'false'

            def replace_quotes(matchobj):
                s = matchobj.group(0).replace(R"\'", R"\\'").replace('"', '\\"')
                s_prime = f'"{s}"'
                return s_prime

            keys = re.compile(r'(?<=[{,\n])([\w\d]+?)(?=:)')
            decimals = re.compile(r'(\.\d+?)(?=[},])')
            bools = re.compile(r'(!\d)')
            flip_quotes = re.compile(r'(?<=[:])(\'.+?\')(?=,)')
            
            res = re.sub(keys, replace_keys, res)
            res = re.sub(decimals, replace_decimals, res)
            res = re.sub(bools, replace_bools, res)
            res = re.sub(flip_quotes, replace_quotes, res)

            return res

        # broke these into two categories cause i wrote them separately and they're kind of different logically? idk
        fixed = prefix_and_suffix_fixes()
        fixed = replace_fixes(fixed)
        
        with open(fixer.fixed_path, 'w') as f:
            f.write(fixed)

if __name__ == '__main__':
    fixer.fix()