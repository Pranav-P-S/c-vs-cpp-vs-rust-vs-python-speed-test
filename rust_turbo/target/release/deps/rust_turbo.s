	.def	@feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
@feat.00 = 0
	.file	"rust_turbo.273e99bcba70d5d6-cgu.0"
	.def	heavy_computation;
	.scl	2;
	.type	32;
	.endef
	.text
	.globl	heavy_computation
	.p2align	4
heavy_computation:
	testq	%rcx, %rcx
	jle	.LBB0_1
	leaq	-1(%rcx), %rax
	leaq	-2(%rcx), %rdx
	mulq	%rdx
	shldq	$63, %rax, %rdx
	leaq	(%rcx,%rdx), %rax
	decq	%rax
	retq
.LBB0_1:
	xorl	%eax, %eax
	retq

