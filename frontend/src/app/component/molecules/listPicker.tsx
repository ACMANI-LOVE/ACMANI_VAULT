import { FormControl, MenuItem, Select, SelectChangeEvent } from "@mui/material"

interface ListSelectorProps {
  list:    string[]
  value:  string
  onChange: (value:string) => void
  noHyphen: boolean
}

const ListSelector = ({list, value, onChange, noHyphen}:ListSelectorProps) => {
  const handleChangeSelect = (e:SelectChangeEvent) => onChange(e.target.value)
  return (<FormControl fullWidth>
    <Select fullWidth size={"small"} value={value} onChange={handleChangeSelect}>
      {(noHyphen) ?? <MenuItem key={-1} value={"-"}>{"-"}</MenuItem>}
      {list.map((item,idx)=><MenuItem
        key={idx}
        value={item}
        >{item}</MenuItem>)}
    </Select>
  </FormControl>)
}

export default ListSelector