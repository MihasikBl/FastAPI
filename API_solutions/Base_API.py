import uvicorn
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

virtual_machine_1 = {
    "OS": "Ubuntu",
    "CPU": 4,
    "RAM": 8,
    "Disk": 64,
    "Owners": ["Mark Perry", "John Travolta", "Will Smith"]
}
virtual_machine_2 = {
    "OS": "Windows Server",
    "CPU": 8,
    "RAM": 16,
    "Disk": 128,
    "Owners": ["Alex Gallagher", "Cameron Diaz", "Billy Butcher"]
}
virtual_machine_3 = {
    "OS": "Windows Server",
    "CPU": 4,
    "RAM": 12,
    "Disk": 64,
    "Owners": ["Alex Smith", "Cameron Thomas", "Billy Milly"]
}
virtual_machine_4 = {
    "OS": "Debian",
    "CPU": 6,
    "RAM": 10,
    "Disk": 256,
    "Owners": ["Donald McDonald", "Justice Young", "Mikey Lawrence"]
}

VM_list = []
VM_list.append(virtual_machine_1)
VM_list.append(virtual_machine_2)
VM_list.append(virtual_machine_3)
VM_list.append(virtual_machine_4)


@app.get("/")
def function():
    return "Hello world"

@app.get("/VirtualMachines", tags=["Virtual Machines"], summary="Output all virtual machines")
def read_VM():
    return VM_list

@app.get("/VirtualMachines/{os_type}",
         tags=["Virtual Machines"],
         summary="Get definite virtual machine")
def get_os(os_type: str):
    for vm in VM_list:
        if str(vm["OS"]) == os_type:
            return vm
    raise HTTPException(status_code=404,detail="OS type is not found")

class NewVM(BaseModel):
    OS: str
    CPU: int
    RAM: int
    Disk: int
    Owners: list

@app.post("/VirtualMachines",
          tags=["Virtual Machines"],
          summary="Add VM in list Virtual Machines")
def create_VM(new_vm: NewVM):
    VM_list.append({
        "OS": new_vm.OS,
        "CPU": new_vm.CPU,
        "RAM": new_vm.RAM,
        "Disk": new_vm.Disk,
        "Owners": new_vm.Owners,
    })
    return {"Status": "Success", "Message": "Your VM successfully added in list"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
