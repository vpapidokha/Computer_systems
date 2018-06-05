.include "defs.h"

.section .bss
envp: .quad 0

.section .text
newline:
.byte '\n'

.global _start

_start:
        movq (%rsp), %rbx
        leaq 16(%rsp,%rbx,8), %rcx
        movq %rcx, envp

loop:
        movq envp, %rcx
        movq (%rcx), %rsi
        movq %rsi, %rdi
        movq $0, %rdx

strlen:
        cmpb $0, (%rdi)
        je cont
        incq %rdi
        incq %rdx
        jmp strlen

cont:
        movq $SYS_WRITE, %rax
        movq $STDOUT, %rdi
        syscall

        addq $8, envp
        movq envp, %r8
        cmpq $0x0, (%r8)
        je end
        cmpq $0,envp
        je end

        movq $SYS_WRITE, %rax
        movq $STDOUT, %rdi
        movq $newline, %rsi
        movq $1, %rdx
        syscall

        jmp loop

end:
        movq $SYS_WRITE, %rax
        movq $STDOUT, %rdi
        movq $newline, %rsi
        movq $1, %rdx
        syscall

        movq $SYS_EXIT, %rax
        movq $0, %rdi
        syscall