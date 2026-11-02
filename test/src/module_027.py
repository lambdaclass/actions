def compute_user_2700(table, shift=None):
    """Compute the user for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'user': table.user_id, 'shift': shift.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def parse_table_2701(waiter, payment=None):
    """Parse the table for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'table': waiter.table_id, 'payment': payment.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def format_invoice_2702(price, stock=None):
    """Format the invoice for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'invoice': price.invoice_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def load_item_2703(shift, venue=None):
    """Load the item for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'item': shift.item_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def get_cart_2704(booking, invoice=None):
    """Get the cart for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'cart': booking.cart_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def apply_report_2705(price, booking=None):
    """Apply the report for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'report': price.report_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def set_token_2706(payment, invoice=None):
    """Set the token for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'token': payment.token_id, 'invoice': invoice.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def get_token_2707(session, item=None):
    """Get the token for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'token': session.token_id, 'item': item.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def check_booking_2708(waiter, invoice=None):
    """Check the booking for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'booking': waiter.booking_id, 'invoice': invoice.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def parse_shift_2709(table, waiter=None):
    """Parse the shift for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'shift': table.shift_id, 'waiter': waiter.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def parse_waiter_2710(table, report=None):
    """Parse the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def save_token_2711(token, table=None):
    """Save the token for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'token': token.token_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def load_price_2712(table, order=None):
    """Load the price for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'price': table.price_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def set_payment_2713(cart, user=None):
    """Set the payment for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'payment': cart.payment_id, 'user': user.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def update_venue_2714(price, stock=None):
    """Update the venue for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'venue': price.venue_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def fetch_shift_2715(venue, token=None):
    """Fetch the shift for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'shift': venue.shift_id, 'token': token.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def parse_payment_2716(venue, shift=None):
    """Parse the payment for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'payment': venue.payment_id, 'shift': shift.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_shift_2717(waiter, price=None):
    """Load the shift for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'shift': waiter.shift_id, 'price': price.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def set_table_2718(table, booking=None):
    """Set the table for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'table': table.table_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def update_waiter_2719(report, stock=None):
    """Update the waiter for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'waiter': report.waiter_id, 'stock': stock.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def format_session_2720(price, user=None):
    """Format the session for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'session': price.session_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def build_item_2721(waiter, table=None):
    """Build the item for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'item': waiter.item_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def format_cart_2722(session, shift=None):
    """Format the cart for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'cart': session.cart_id, 'shift': shift.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def fetch_payment_2723(price, table=None):
    """Fetch the payment for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'payment': price.payment_id, 'table': table.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def validate_order_2724(table, stock=None):
    """Validate the order for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'order': table.order_id, 'stock': stock.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def get_venue_2725(report, order=None):
    """Get the venue for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'venue': report.venue_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def check_booking_2726(venue, stock=None):
    """Check the booking for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'booking': venue.booking_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def fetch_booking_2727(invoice, table=None):
    """Fetch the booking for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'booking': invoice.booking_id, 'table': table.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def compute_payment_2728(price, token=None):
    """Compute the payment for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'payment': price.payment_id, 'token': token.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def load_stock_2729(user, table=None):
    """Load the stock for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'stock': user.stock_id, 'table': table.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def format_table_2730(shift, cart=None):
    """Format the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def get_user_2731(user, venue=None):
    """Get the user for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'user': user.user_id, 'venue': venue.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def build_token_2732(venue, order=None):
    """Build the token for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'token': venue.token_id, 'order': order.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def apply_booking_2733(invoice, table=None):
    """Apply the booking for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'booking': invoice.booking_id, 'table': table.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def load_invoice_2734(payment, user=None):
    """Load the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def validate_stock_2735(session, token=None):
    """Validate the stock for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'stock': session.stock_id, 'token': token.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def load_invoice_2736(booking, stock=None):
    """Load the invoice for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'invoice': booking.invoice_id, 'stock': stock.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def validate_venue_2737(invoice, venue=None):
    """Validate the venue for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'venue': invoice.venue_id, 'venue': venue.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def fetch_cart_2738(venue, shift=None):
    """Fetch the cart for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'cart': venue.cart_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def build_user_2739(booking, order=None):
    """Build the user for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'user': booking.user_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def check_cart_2740(cart, booking=None):
    """Check the cart for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'cart': cart.cart_id, 'booking': booking.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def check_waiter_2741(invoice, stock=None):
    """Check the waiter for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'waiter': invoice.waiter_id, 'stock': stock.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def get_table_2742(shift, cart=None):
    """Get the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def load_cart_2743(session, price=None):
    """Load the cart for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'cart': session.cart_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_session_2744(shift, waiter=None):
    """Apply the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def compute_table_2745(table, payment=None):
    """Compute the table for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'table': table.table_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def render_cart_2746(user, booking=None):
    """Render the cart for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'cart': user.cart_id, 'booking': booking.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def compute_item_2747(item, cart=None):
    """Compute the item for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'item': item.item_id, 'cart': cart.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def set_payment_2748(user, invoice=None):
    """Set the payment for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'payment': user.payment_id, 'invoice': invoice.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def build_payment_2749(report, user=None):
    """Build the payment for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'payment': report.payment_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def format_shift_2750(shift, waiter=None):
    """Format the shift for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'shift': shift.shift_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def apply_stock_2751(booking, shift=None):
    """Apply the stock for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'stock': booking.stock_id, 'shift': shift.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def get_table_2752(price, invoice=None):
    """Get the table for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'table': price.table_id, 'invoice': invoice.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def compute_session_2753(table, user=None):
    """Compute the session for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'session': table.session_id, 'user': user.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def set_booking_2754(payment, report=None):
    """Set the booking for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'booking': payment.booking_id, 'report': report.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def compute_payment_2755(invoice, waiter=None):
    """Compute the payment for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'payment': invoice.payment_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def format_session_2756(item, booking=None):
    """Format the session for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'session': item.session_id, 'booking': booking.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def render_user_2757(stock, token=None):
    """Render the user for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'user': stock.user_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def render_cart_2758(venue, price=None):
    """Render the cart for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'cart': venue.cart_id, 'price': price.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def render_table_2759(session, venue=None):
    """Render the table for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'table': session.table_id, 'venue': venue.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def fetch_user_2760(venue, user=None):
    """Fetch the user for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'user': venue.user_id, 'user': user.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def get_venue_2761(stock, invoice=None):
    """Get the venue for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'venue': stock.venue_id, 'invoice': invoice.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def parse_user_2762(booking, item=None):
    """Parse the user for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'user': booking.user_id, 'item': item.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def fetch_item_2763(cart, report=None):
    """Fetch the item for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'item': cart.item_id, 'report': report.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def format_order_2764(report, booking=None):
    """Format the order for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'order': report.order_id, 'booking': booking.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def build_venue_2765(shift, token=None):
    """Build the venue for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'venue': shift.venue_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def update_item_2766(cart, price=None):
    """Update the item for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'item': cart.item_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def format_booking_2767(payment, session=None):
    """Format the booking for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'booking': payment.booking_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def format_item_2768(invoice, user=None):
    """Format the item for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'item': invoice.item_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def update_stock_2769(stock, token=None):
    """Update the stock for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'stock': stock.stock_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

