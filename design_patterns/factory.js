function Developer(name) {
	this.name = name;
	this.type = "Developer";
}

function Tester(name) {
	this.name = name;
	this.type = "Tester";
}

function say() {
	console.log(`My name is ${this.name} and I am a ${this.type}.`);
}

function EmployeeFactory() {
	this.create = (name, type) => {
		switch(type) {
			case 1:
				return new Developer(name)
				break;
			case 2:
				return new Tester(name)
				break;
		}
	}
}

const employees = []
const employeeFactory = new EmployeeFactory()

employees.push(employeeFactory.create('Jane', 1));
employees.push(employeeFactory.create('John', 2));

employees.forEach(emp => {
	say.call(emp);
})
