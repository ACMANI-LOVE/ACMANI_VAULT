import { FormControl, MenuItem, Select, SelectChangeEvent } from "@mui/material"

interface ListSelectorProps {
  list:     string[]
  select:  number
  onChange: (idx:number) => void
}

const ListSelector = ({list, select, onChange}:ListSelectorProps) => {
  const handleChangeSelect = (e:SelectChangeEvent) => onChange(Number(e.target.value))
  return (<FormControl fullWidth>
    <Select fullWidth size={"small"} value={`${select}`} onChange={handleChangeSelect}>
      <MenuItem key={-1} value={-1}>{"-"}</MenuItem>
      {list.map((item,idx)=><MenuItem
        key={idx}
        value={idx}
        >{item}</MenuItem>)}
    </Select>
  </FormControl>)
}

export default ListSelector