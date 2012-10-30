/* Do not edit this file. It was automatically generated. */

#ifndef HEADER_ProcessList
#define HEADER_ProcessList
/*
htop - ProcessList.h
(C) 2004,2005 Hisham H. Muhammad
Released under the GNU GPL, see the COPYING file
in the source distribution for its full text.
*/

/* Darwin reference:
 *
 * http://web.mit.edu/darwin/src/modules/xnu/osfmk/man/
 *
 */

#ifndef CONFIG_H
#define CONFIG_H
#include "config.h"
#endif

#include "Process.h"
#include "Vector.h"
#include "UsersTable.h"
#include "Hashtable.h"
#include "String.h"

#include <dirent.h>
#include <mach/host_info.h>
#include <mach/mach_host.h>
#include <mach/mach_init.h>
#include <mach/mach_interface.h>
#include <mach/mach_port.h>
#include <mach/mach_traps.h>
#include <mach/mach_types.h>
#include <mach/machine.h>
#include <mach/processor_info.h>
#include <mach/shared_memory_server.h>
#include <mach/task.h>
#include <mach/thread_act.h>
#include <mach/time_value.h>
#include <mach/vm_map.h>
#include <sys/proc.h>
#include <sys/resource.h>
#include <sys/stat.h>
#include <sys/sysctl.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/utsname.h>
#include <unistd.h>

#include <signal.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "debug.h"
#include "util.h"
#include <assert.h>

#ifndef MAX_NAME
#define MAX_NAME 128
#endif

#ifndef MAX_READ
#define MAX_READ 2048
#endif

#ifndef PER_PROCESSOR_FIELDS
#define PER_PROCESSOR_FIELDS 22
#endif

#define KI_PROC(ki) (&(ki)->ki_p->kp_proc)
#define KI_EPROC(ki) (&(ki)->ki_p->kp_eproc)
#define STATE_MAX       7

#ifdef DEBUG_PROC
typedef int ( *vxscanf ) ( void *, const char *, va_list );
#endif

typedef struct ProcessList_ {
  Vector *processes;
  Vector *processes2;
  Hashtable *processTable;
  Process *prototype;
  UsersTable *usersTable;

  int processorCount;
  int totalTasks;
  int runningTasks;
  vm_size_t pageSize;

  // Must match number of PER_PROCESSOR_FIELDS constant
  unsigned long long int *totalTime;
  unsigned long long int *userTime;
  unsigned long long int *systemTime;
  unsigned long long int *systemAllTime;
  unsigned long long int *idleAllTime;
  unsigned long long int *idleTime;
  unsigned long long int *niceTime;
  unsigned long long int *ioWaitTime;
  unsigned long long int *irqTime;
  unsigned long long int *softIrqTime;
  unsigned long long int *stealTime;
  unsigned long long int *totalPeriod;
  unsigned long long int *userPeriod;
  unsigned long long int *systemPeriod;
  unsigned long long int *systemAllPeriod;
  unsigned long long int *idleAllPeriod;
  unsigned long long int *idlePeriod;
  unsigned long long int *nicePeriod;
  unsigned long long int *ioWaitPeriod;
  unsigned long long int *irqPeriod;
  unsigned long long int *softIrqPeriod;
  unsigned long long int *stealPeriod;

  unsigned long long int totalMem;
  unsigned long long int usedMem;
  unsigned long long int freeMem;
  unsigned long long int sharedMem;
  unsigned long long int buffersMem;
  unsigned long long int cachedMem;
  unsigned long long int totalSwap;
  unsigned long long int usedSwap;
  unsigned long long int freeSwap;

  ProcessField *fields;
  ProcessField sortKey;
  int direction;
  bool hideThreads;
  bool shadowOtherUsers;
  bool hideKernelThreads;
  bool hideUserlandThreads;
  bool treeView;
  bool highlightBaseName;
  bool highlightMegabytes;
  bool highlightThreads;
  bool detailedCPUTime;
#ifdef DEBUG_PROC
  FILE *traceFile;
#endif

} ProcessList;

typedef struct thread_values {
  struct thread_basic_info tb;
  union {
    struct policy_timeshare_info tshare;
    struct policy_rr_info rr;
    struct policy_fifo_info fifo;
  } schedinfo;
} thread_values_t;

struct usave {
  struct timeval u_start;
  struct rusage u_ru;
  struct rusage u_cru;
  char u_acflag;
  char u_valid;
};

typedef struct kinfo {
  struct kinfo_proc *ki_p;
  struct usave ki_u;
  char *ki_args;
  char *ki_env;
  task_port_t task;
  int state;
  int cpu_usage;
  int curpri;
  int basepri;
  int swapped;
  struct task_basic_info tasks_info;
  struct task_thread_times_info times;
  union {
    struct policy_timeshare_info tshare;
    struct policy_rr_info rr;
    struct policy_fifo_info fifo;
  } schedinfo;
  int invalid_tinfo;
  mach_msg_type_number_t thread_count;
  thread_port_array_t thread_list;
  thread_values_t *thval;
  int invalid_thinfo;
  vm_size_t shared;
  int swapped_pages;
} KINFO;

ProcessList *ProcessList_new( UsersTable * usersTable );
void ProcessList_delete( ProcessList * this );
void ProcessList_invertSortOrder( ProcessList * this );
RichString ProcessList_printHeader( ProcessList * this );
Process *ProcessList_get( ProcessList * this, int index );
int ProcessList_size( ProcessList * this );
void ProcessList_sort( ProcessList * this );
void ProcessList_scan( ProcessList * this );
ProcessField ProcessList_keyAt( ProcessList * this, int at );

#endif