# Program name
PROGRAM = a.out

JCC = javac
JAR = jar

# Directories
SRC = ./src/
OBJ = ./obj/
BIN = ./bin/

# Flags
FLAGS = -g

# Source files
PRELIMSOURCES=$(shell find $(SRC) -name '*.java')
SOURCES=$(PRELIMSOURCES:$(SRC)%=%)

# Object files that mirror the source files
OBJECTS=$(SOURCES:.java=.class)

# Prefixed Source files
PREFIXED_SOURCES=$(addprefix $(SRC),$(SOURCES))

# Prefixed Object files
PREFIXED_OBJECTS=$(addprefix $(OBJ),$(OBJECTS))

# Prefixed Program name
PREFIXED_PROGRAM=$(addprefix $(BIN),$(PROGRAM))

# Make 'all' instructions
all: $(PREFIXED_OBJECTS) $(PREFIXED_PROGRAM)

# Make '$(PROGRAM)' instructions
$(PREFIXED_PROGRAM): $(PREFIXED_OBJECTS)
	@mkdir -p $(@D) # Makes the 'bin' directory if it doesn't exist
	$(JAR) cfm $@ $(SRC)Manifest -C $(OBJ) .
	@chmod 777 $(PREFIXED_PROGRAM)

# Make '$(OBJECTS)' instructions
$(OBJ)%.class: $(SRC)%.java
	@mkdir -p $(OBJ) # Makes the 'obj' directory if it doesn't exist
	$(JCC) -d $(OBJ) $(PREFIXED_SOURCES)


# Make 'clean' instructions
# 'dir' gets the directories of the object files
# 'sort' sorts the directories and removes duplicates
# 'add*' is pretty self-explanatory 
clean:
	rm -f $(addprefix $(OBJ), $(addsuffix *.class, $(sort $(dir $(OBJECTS)))))
