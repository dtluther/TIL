interface Builder {
	producePartA(): void;
	productPartB(): void;
	productPartC(): void;
}

class ConcreteBuilder1 implements Builder {
	private product: Product1;
	
	constructor() {
		this.reset();
	}

	public reset(): void {
		this.product = new Product1();
	}

	public producePartA(): void {
		this.product.parts.push('PartA1');
	}

	public producePartB(): void {
		this.product.parts.push('PartB1');
	}

	public productPartV(): void {
		this.product.parts.push('PartC1');
	}

	public getProduct(): Product1 {
		const result = this.product;
		this.reset();
		return result;
	}
}	

class Product1 {
	// public parts: Array<string> = [];
	public parts: string[] = [];

	public listParts(): void {
		console.log(`Product parts: ${this.parts.join(', ')}`);
	}
}

class Director {
	private builder: Builder;

	public setBuilder(builder: Builder): void {
		this.builder = builder;
	}

	public buildMinimumViableProduct(): void {
		this.builder.producePartA();
	}

	public buildFullFeaturedProduct(): void {
		this.builder.producePartA();
		this.builder.producePartB();
		this.builder.producePartC();
	}
}

const clientCode: (director: Director): void => {
	const builder = new ConcreteBuilder1();
	director.setBuilder(builder);

	console.log('Standard basic product:');
	director.buildMinimumViableProduct();
	builder.getProduct().listParts()
}
